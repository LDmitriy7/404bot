from aiogram import Bot, Dispatcher, executor, types

from . import events
from .handler import Handler, Callback
from .update_context import UpdateContext


class App:
    def __init__(self, bot_token: str, handlers: list[Handler]):
        self._bot = Bot(bot_token, parse_mode='html')
        self._dp = Dispatcher(self._bot)
        self._setup_handlers(handlers)

    def _setup_handlers(self, handlers: list[Handler]):
        for handler in handlers:
            self._setup_handler(handler)

    def _setup_handler(self, handler: Handler):
        event = handler.event

        if isinstance(event, events.Command):
            decorator = self._dp.message_handler(commands=event.value, chat_type=event.chat_type)
        else:
            raise ValueError('Invalid handler')

        decorator(self._adapt_callback(handler.callback))

    def _adapt_callback(self, callback: Callback):
        async def wrapper(_):
            update = types.Update.get_current()
            ctx = UpdateContext(self._bot, update)
            await callback(ctx)

        return wrapper

    def run(self):
        executor.start_polling(self._dp)
