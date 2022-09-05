from aiogram import Dispatcher, executor, types

from .bot import Bot
from .chat_data import BaseChatData
from .database import BaseDatabase
from .handler import Handler, Callback
from .handler_group import HandlerGroup
from .storage import BaseStorage
from .update_context import UpdateContext


class App:
    def __init__(self, bot: Bot, db: BaseDatabase):
        self._bot = getattr(bot, '_raw')
        self._dp = Dispatcher(self._bot, storage=db.storage)

    def _setup_handlers(self, handlers: HandlerGroup):
        for handler in handlers:
            self._setup_handler(handler)

    def _setup_handler(self, handler: Handler):
        event = handler.event
        decorator = event.adapt(self._dp)
        decorator(self._adapt_callback(handler.callback))

    async def _make_storage(self):
        raw_storage = self._dp.current_state()
        storage_data = await raw_storage.get_data()
        return BaseStorage(storage_data)

    async def _make_chat_data(self):
        chat = types.Chat.get_current()
        chat_data = await self._dp.storage.get_data(chat=chat.id)
        return BaseChatData(chat_data)

    async def _save_storage(self, storage: BaseStorage):
        raw_storage = self._dp.current_state()
        await raw_storage.set_data(storage.__data__)

    async def _save_chat_data(self, chat_data: BaseChatData):
        chat = types.Chat.get_current()
        await self._dp.storage.set_data(chat=chat.id, data=chat_data.__data__)

    def _adapt_callback(self, callback: Callback):
        async def wrapper(_):
            update = types.Update.get_current()
            storage = await self._make_storage()
            chat_data = await self._make_chat_data()
            ctx = UpdateContext(self._bot, update)
            await callback(ctx)
            await self._save_storage(storage)
            await self._save_chat_data(chat_data)

        return wrapper

    def run(self, handlers: HandlerGroup):
        self._setup_handlers(handlers)
        executor.start_polling(self._dp)
