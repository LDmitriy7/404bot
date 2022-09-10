import inspect
from typing import Callable, Iterable

from aiogram import Dispatcher, executor, types

from .bot import Bot
from .chat_data import BaseChatData
from .database import BaseDatabase
from .handler import Handler, Callback
from .handler_group import HandlerGroup
from .start_params import BaseStartParams
from .storage import BaseStorage
from .update_context import UpdateContext


class App:
    def __init__(self, bot: Bot, db: BaseDatabase):
        self._bot = getattr(bot, '_raw')
        self._dp = Dispatcher(self._bot)
        self._db = db

    def run(self, handlers: HandlerGroup):
        self._setup_handlers(handlers)
        executor.start_polling(self._dp)

    def _setup_handlers(self, handlers: HandlerGroup):
        for handler in handlers:
            self._setup_handler(handler)

    def _setup_handler(self, handler: Handler):
        decorator = handler.event.adapt(self._dp)
        decorator(self._adapt_callback(handler.callback))

    def _adapt_callback(self, callback: Callback):
        async def wrapper(_):
            await self._run_callback(callback)

        return wrapper

    async def _run_callback(self, callback: Callback):
        kwargs = self._make_callback_kwargs(callback)
        await callback(**kwargs)
        self._save_callback_args(kwargs.values())

    def _make_callback_kwargs(self, callback: Callback):
        arg_types = get_arg_types(callback)
        return {arg: self._make_callback_arg(arg_types[arg]) for arg in arg_types}

    def _make_callback_arg(self, arg_type: type):
        if issubclass(arg_type, UpdateContext):
            return self._create_context()
        if issubclass(arg_type, BaseChatData):
            return self._create_chat_data()
        if issubclass(arg_type, BaseStartParams):
            return self._create_start_params()
        if issubclass(arg_type, BaseStorage):
            return self._create_storage()
        raise TypeError(f'Invalid callback argument type: {arg_type}')

    def _create_context(self):
        update = types.Update.get_current()
        return UpdateContext(self._bot, update)

    def _create_chat_data(self):
        chat = types.Chat.get_current()
        data = self._db.get_chat_data(chat.id)
        return BaseChatData(data)

    def _create_start_params(self):
        params = {}
        message = types.Message.get_current()
        if params_id := message.get_args():
            params = self._db.get_start_params(params_id)
        return BaseStartParams(params)

    def _create_storage(self):
        chat = types.Chat.get_current()
        user = types.User.get_current()
        data = self._db.get_storage_data(chat.id, user.id)
        return BaseStorage(data)

    def _save_callback_args(self, args: Iterable):
        for arg in args:
            if isinstance(arg, BaseChatData):
                self._save_chat_data(arg)
            if isinstance(arg, BaseStorage):
                self._save_storage(arg)

    def _save_chat_data(self, chat_data: BaseChatData):
        chat = types.Chat.get_current()
        self._db.set_chat_data(chat.id, chat_data.__data__)

    def _save_storage(self, storage: BaseStorage):
        chat = types.Chat.get_current()
        user = types.User.get_current()
        self._db.set_storage_data(chat.id, user.id, storage.__data__)


def get_arg_types(func: Callable) -> dict[str, type]:
    return inspect.getfullargspec(func).annotations
