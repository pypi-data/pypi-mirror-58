import logging
import time
from typing import TYPE_CHECKING, Optional, Callable, Any
from dataclasses import dataclass
from pystrict import strict
from .exceptions import CloudTemporaryError, CloudDisconnectedError, CloudCursorError, CloudTokenError
from .runnable import Runnable
from .muxer import Muxer
from .types import OType, DIRECTORY
from .notification import SourceEnum

if TYPE_CHECKING:
    from cloudsync.sync import SyncState
    from cloudsync import Provider
    from cloudsync.notification import NotificationManager

log = logging.getLogger(__name__)


@dataclass
class Event:
    otype: OType                           # fsobject type     (DIRECTORY or FILE)
    oid: str                               # fsobject id
    path: Optional[str]                    # path
    hash: Any                              # fsobject hash     (better name: ohash)
    exists: Optional[bool]
    mtime: Optional[float] = None
    prior_oid: Optional[str] = None        # path basesd systems use this on renames
    new_cursor: Optional[str] = None


@strict             # pylint: disable=too-many-instance-attributes
class EventManager(Runnable):
    def __init__(self, provider: "Provider", state: "SyncState", side: int,
                 notification_manager: Optional["NotificationManager"] = None,
                 walk_root: Optional[str] = None, reauth: Callable[[], None] = None):
        log.debug("provider %s, root %s", provider.name, walk_root)
        self.provider = provider
        assert self.provider.connection_id
        self.label: str = f"{self.provider.name}:{self.provider.connection_id}"
        self.events = Muxer(provider.events, restart=True)
        self.state: 'SyncState' = state
        self.side: int = side
        self._cursor_tag: str = self.label + "_cursor"
        self.__nmgr = notification_manager
        self.need_auth = False

        self.cursor = self.state.storage_get_data(self._cursor_tag)

        if self.cursor is not None:
            log.debug("retrieved existing cursor %s for %s", self.cursor, self.provider.name)
            try:
                self.provider.current_cursor = self.cursor
            except CloudCursorError as e:
                log.exception("Cursor error... resetting cursor. %s", e)
                self.cursor = None

        self.walk_root = walk_root
        self.need_walk = False
        self._first_do = True
        self._walk_tag: Optional[str] = None
        if self.walk_root:
            self._walk_tag = self.label + "_walked_" + self.walk_root
            if self.cursor is None or self.state.storage_get_data(self._walk_tag) is None:
                self.need_walk = True

        self.min_backoff = provider.default_sleep / 10
        self.max_backoff = provider.default_sleep * 10
        self.mult_backoff = 2

        self.reauthenticate = reauth or self.__reauth

    def __reauth(self):
        self.provider.connect(self.provider.authenticate())

    def forget(self):
        if self._walk_tag is not None:
            self.state.storage_delete_tag(self._walk_tag)
        if self._cursor_tag is not None:
            self.state.storage_delete_tag(self._cursor_tag)

    @property
    def busy(self):
        return not self.events.empty or self.need_walk

    def do(self):
        self.events.shutdown = False
        try:
            if not self.provider.connected:
                if self.need_auth:
                    try:
                        # possibly this is a temporary loss of authorization
                        self.provider.reconnect()
                    except CloudTokenError:
                        log.warning("Need auth, calling reauthenticate")
                        try:
                            self.reauthenticate()
                        except NotImplementedError:
                            raise CloudTokenError("No auth method defined")
                    self.need_auth = False
                else:
                    log.info("reconnect to %s", self.provider.name)
                    self.provider.reconnect()
            self._do_unsafe()
        except (CloudTemporaryError, CloudDisconnectedError) as e:
            log.warning("temporary error %s[%s] in event watcher", type(e), e)
            if self.__nmgr:
                self.__nmgr.notify_from_exception(SourceEnum(self.side), e)
            self.backoff()
        except CloudCursorError as e:
            log.exception("Cursor error... resetting cursor. %s", e)
            self.provider.current_cursor = self.provider.latest_cursor
            self._save_current_cursor()
            self.backoff()
        except CloudTokenError:
            # this is separated from the main block because
            # it can be raised during reconnect in the exception handler and in do_unsafe
            self.need_auth = True
            self.backoff()

    def _do_unsafe(self):
        if self._first_do:
            if self.cursor is None:
                self.cursor = self.provider.current_cursor
                if self.cursor is not None:
                    self.state.storage_update_data(self._cursor_tag, self.cursor)
        self._first_do = False

        if self.need_walk:
            log.debug("walking all %s/%s files as events, because no working cursor on startup",
                      self.provider.name, self.walk_root)
            for event in self.provider.walk(self.walk_root):
                self.process_event(event, from_walk=True)
            self.state.storage_update_data(self._walk_tag, time.time())
            self.need_walk = False

        for event in self.events:
            if not event:
                log.error("%s got BAD event %s", self.label, event)
                continue
            self.process_event(event)

        self._save_current_cursor()

    def _save_current_cursor(self):
        current_cursor = self.provider.current_cursor

        if current_cursor != self.cursor:
            self.state.storage_update_data(self._cursor_tag, current_cursor)
            self.cursor = current_cursor

    def _drain(self):
        # for tests, delete events
        for _ in self.events:
            pass

    def process_event(self, event: Event, from_walk=False):
        with self.state.lock:
            log.debug("%s got event %s", self.label, event)
            path = event.path
            exists = event.exists
            otype = event.otype
            ehash = event.hash
            info = None

            if event.oid is None:
                if not event.exists and event.path and event.otype == DIRECTORY:
                    # allow no oid on deletion of folders
                    # this is because of dropbox
                    known = self.state.lookup_path(self.side, event.path)
                    if known:
                        log.debug("using known oid for %s", event.path)
                        event.oid = known[0][self.side].oid

            if event.oid is None:
                log.warning("ignoring event %s, no oid", event)
                return

            if from_walk or not event.path and not self.state.lookup_oid(self.side, event.oid):
                info = self.provider.info_oid(event.oid)
                if info:
                    if info.otype != event.otype:
                        log.warning("provider %s gave a bad event: %s != %s, using %s",
                                    self.provider.name, info.path, event.otype, info.otype)
                    path = info.path
                    otype = info.otype
                    ehash = info.hash

            if from_walk:
                # this event is from a walk, and we're checking to see if the state has changed
                already = self.state.lookup_oid(self.side, event.oid)
                if already:
                    changed = already[self.side].hash != ehash or already[self.side].path != path
                    if not changed:
                        return

            self.state.update(self.side, otype, event.oid, path=path, hash=ehash,
                              exists=exists, prior_oid=event.prior_oid)
            self.state.storage_commit()

    def stop(self, forever=True):
        if forever:
            self.events.shutdown = True
        super().stop(forever=forever)
