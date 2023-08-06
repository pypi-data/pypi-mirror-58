import logging
from contextlib import suppress
from typing import TYPE_CHECKING, Optional, Dict, Tuple, Iterator, overload
from typing_extensions import Literal
from ehforwarderbot import coordinator
from ehforwarderbot.chat import EFBChat
from ehforwarderbot.constants import ChatType
from ehforwarderbot.types import ModuleID, ChatID
from ehforwarderbot.exceptions import EFBChatNotFound

from .chat import ETMChat

if TYPE_CHECKING:
    from . import TelegramChannel

CacheKey = Tuple[ModuleID, ChatID, Optional[ChatID]]
"""Cache storage key: module_id, chat_id, group_id (if available)"""


class ChatObjectCacheManager:
    """Maintain and update chat objects from all slave channels and
    middlewares.
    """

    def __init__(self, channel: 'TelegramChannel'):
        self.channel = channel
        self.db = channel.db
        self.logger = logging.getLogger(__name__)

        self.self = ETMChat(db=self.db, channel=self.channel).self()
        self.cache: Dict[CacheKey, ETMChat] = dict()
        self.enrol(self.self)

        # load all chats from all slave channels and convert to ETMChat object
        for channel_id, module in coordinator.slaves.items():
            # noinspection PyBroadException
            try:
                chats = module.get_chats()
            except Exception:
                continue
            for chat in chats:
                self.compound_enrol(chat)

    def compound_enrol(self, chat: EFBChat) -> ETMChat:
        """Convert and enrol a chat object for the first time.
        This method also enrols all members if the chat is a group.
        If the chat is a group member, it will try to match its group in cache
        first, and re-cache it if not found.
        """
        etm_chat = ETMChat(db=self.db, chat=chat)
        if chat.group:
            group_key = self.get_cache_key(chat.group)
            if group_key in self.cache:
                cached_group = self.cache[group_key]
                cached_group.members.append(etm_chat)
                etm_chat.group = cached_group
                self.enrol(etm_chat)
                return etm_chat
            else:
                cached_group = self.compound_enrol(chat.group)
                chat_key = self.get_cache_key(chat)
                if chat_key in self.cache:
                    return self.cache[chat_key]
                else:
                    cached_group.members.append(etm_chat)
                    etm_chat.group = cached_group
                    self.enrol(etm_chat)
                    return etm_chat

        if etm_chat.chat_type == ChatType.Group:
            self.logger.debug("Compound enrol %s members of group %s", len(etm_chat.members), etm_chat)
            for i in etm_chat.members:
                self.enrol(i)
            group_self = ETMChat(db=self.db, channel=self.channel)
            group_self.group = etm_chat
            group_self.is_chat = False
            group_self.self()
            self.enrol(group_self)
        self.enrol(etm_chat)

        return etm_chat

    def enrol(self, chat: ETMChat):
        """Add a chat object to the cache storage *for the first time*.

        This would not update the cached object upon conflicting.
        """
        key = self.get_cache_key(chat)
        self.cache[key] = chat
        self.logger.debug("Enrolling key %s with value %s", key, chat)

    @staticmethod
    def get_cache_key(chat: EFBChat) -> CacheKey:
        module_id = chat.module_id
        chat_id = chat.chat_uid
        group_id = None
        if chat.group:
            group_id = chat.group.chat_uid
        return module_id, chat_id, group_id

    def get_self(self, group_id: Optional[ChatID] = None) -> ETMChat:
        return self.get_chat(self.channel.channel_id, ETMChat.SELF_ID, group_id=group_id, build_dummy=True)

    @overload
    def get_chat(self, module_id: ModuleID, chat_id: ChatID,
                 group_id: Optional[ChatID] = None, build_dummy: Literal[True] = True) -> ETMChat: ...

    @overload
    def get_chat(self, module_id: ModuleID, chat_id: ChatID,
                 group_id: Optional[ChatID] = None, build_dummy: bool = False) -> Optional[ETMChat]: ...

    def get_chat(self, module_id: ModuleID, chat_id: ChatID,
                 group_id: Optional[ChatID] = None, build_dummy: bool = False) -> Optional[ETMChat]:
        """
        Get an ETMChat object of a chat from cache.

        If the object queried is not found, try to get from database cache,
        then the relevant channel.
        If still not found, return None.

        If build_dummy is set to True, this will return a dummy object with
        the module_id, chat_id and group_id specified.
        """
        key = (module_id, chat_id, group_id)
        if key in self.cache:
            return self.cache[key]
        # TODO: Should it return unassociated chat object if the one in group is not found?
        # key = (channel, chat_id, None)
        # if key in self.cache:
        #     return self.cache[key]

        c_log = self.db.get_slave_chat_info(module_id, chat_id, group_id)
        if c_log is not None and c_log.pickle:
            obj = ETMChat.unpickle(c_log.pickle, self.db)
            self.compound_enrol(obj)
            return obj

        # Only look up from slave channels as middlewares don’t have get_chat_by_id method.
        if module_id in coordinator.slaves:
            with suppress(EFBChatNotFound):
                chat_obj = coordinator.slaves[module_id].get_chat(chat_id, group_id)
                return self.compound_enrol(chat_obj)

        if build_dummy:
            chat = ETMChat(db=self.db,
                           module_id=module_id,
                           module_name=module_id,
                           chat_uid=chat_id,
                           chat_name=chat_id)
            if group_id:
                group = ETMChat(db=self.db,
                                module_id=module_id,
                                module_name=module_id,
                                chat_uid=group_id,
                                chat_name=group_id)
                chat.group = group
                chat.is_chat = False
            return chat
        return None

    def update_chat_obj(self, chat: EFBChat, full_update: bool = False) -> ETMChat:
        """Insert or update chat object to cache.
        Only checking name and alias, not checking group/member association,
        unless full update is requested.
        """
        key = self.get_cache_key(chat)
        self.logger.debug("Trying to update key %s with object %s. Full update: %s", key, chat, full_update)
        if key not in self.cache:
            self.logger.debug("Key %s is not in cache. Do compound enrol.", key)
            return self.compound_enrol(chat)

        cached = self.cache[key]
        self.logger.debug("Cached object found with key %s.", key)

        if full_update:
            cached.chat_name = chat.chat_name
            cached.chat_alias = chat.chat_alias
            cached.chat_type = chat.chat_type
            cached.is_chat = chat.is_chat
            cached.has_self = chat.has_self
            cached.description = chat.description
            cached.vendor_specific = chat.vendor_specific
            cached.notification = chat.notification
            cached.members = [self.update_chat_obj(i, full_update) for i in chat.members]
            cached.update_to_db()
        else:
            if chat.chat_name != cached.chat_name or \
                    chat.chat_alias != cached.chat_alias or \
                    chat.notification != cached.notification or \
                    chat.description != cached.description:
                cached.chat_name = chat.chat_name
                cached.chat_alias = chat.chat_alias
                cached.notification = chat.notification
                cached.description = chat.description
                cached.update_to_db()
        return cached

    def delete_chat_object(self, module_id: ModuleID, chat_id: ChatID, group_id: Optional[ChatID] = None):
        """Remove chat object from cache.

        Removing members of a group too if available.
        """
        key = (module_id, chat_id, group_id)
        if key not in self.cache:
            return
        chat = self.cache.pop(key)
        if chat.members:
            for i in chat.members:
                key = (module_id, i.chat_uid, chat_id)
                if key in self.cache:
                    del self.cache[key]

    @property
    def all_chats(self) -> Iterator[ETMChat]:
        """Return all chats that is not a group member and not myself."""
        return (val for key, val in self.cache.items() if
                key[2] is None and val.is_chat and not val.is_self
                )
