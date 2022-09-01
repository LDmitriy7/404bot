from aiogram import types, Bot

from .inline_keyboard import InlineKeyboard


class UpdateContext:
    def __init__(self, bot: Bot, update: types.Update):
        self._bot = bot
        self._update = update

    async def send_message(self, text: str, keyboard: InlineKeyboard = None):
        chat_id = self._update.message.chat.id
        reply_markup = keyboard.adapt() if keyboard else None
        await self._bot.send_message(chat_id, text, reply_markup=reply_markup)

    @property
    def user(self) -> types.User:
        return self._update.message.from_user

    @property
    def me(self) -> types.User:
        return getattr(self._bot, '_me')
