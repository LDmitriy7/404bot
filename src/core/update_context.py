from aiogram import types, Bot

from .keyboards import AnyKeyboard


class UpdateContext:
    def __init__(self, bot: Bot, update: types.Update):
        self._bot = bot
        self._update = update

    @property
    def message(self):
        update = self._update

        if message := update.message:
            return message
        if query := update.callback_query:
            return query.message

    @property
    def text(self):
        if message := self.message:
            return message.text

    @property
    def query(self):
        update = self._update

        if query := update.callback_query:
            return query

    @property
    def chat(self):
        if message := self.message:
            return message.chat

    @property
    def user(self):
        if message := self.message:
            return message.from_user
        if query := self.query:
            return query.from_user

    @property
    def me(self) -> types.User:
        return getattr(self._bot, '_me')

    def send_message(self, text: str, keyboard: AnyKeyboard = None):
        reply_markup = keyboard.adapt() if keyboard else None
        return self._bot.send_message(self.chat.id, text, reply_markup=reply_markup)

    def send_photo(self, photo_id: str, keyboard: AnyKeyboard = None):
        reply_markup = keyboard.adapt() if keyboard else None
        return self._bot.send_photo(self.chat.id, photo_id, reply_markup=reply_markup)

    def send_media_group(self, photo_ids: list[str]):
        media = [types.InputMediaPhoto(media=i) for i in photo_ids]
        return self._bot.send_media_group(self.chat.id, media=media)

    def delete_message(self):
        return self._bot.delete_message(self.chat.id, self.message.message_id)
