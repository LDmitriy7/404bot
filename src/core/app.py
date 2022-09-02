import inspect

from aiogram import Bot, Dispatcher, executor, types

from .database import BaseDatabase
from .handler import Handler, Callback
from .update_context import UpdateContext
from .user_data import BaseUserData


class App:
    def __init__(self, bot_token: str, database: BaseDatabase):
        self._bot = Bot(bot_token, parse_mode='html')
        self._dp = Dispatcher(self._bot)
        self._db = database

    def _setup_handlers(self, handlers: list[Handler]):
        for handler in handlers:
            self._setup_handler(handler)

    def _setup_handler(self, handler: Handler):
        event = handler.event
        decorator = event.adapt(self._dp)
        decorator(self._adapt_callback(handler.callback))

    def _adapt_callback(self, callback: Callback):
        async def wrapper(_):
            update = types.Update.get_current()
            ctx = UpdateContext(self._bot, update)
            args_count = count_args(callback)

            if args_count == 1:
                await callback(ctx)
            elif args_count == 2:
                await callback(ctx, self._db)
            else:
                await callback(ctx, self._db, BaseUserData())

        return wrapper

    def run(self, handlers: list[Handler]):
        self._setup_handlers(handlers)
        executor.start_polling(self._dp)


def count_args(func):
    full_args = inspect.getfullargspec(func)
    return len(full_args.args)
