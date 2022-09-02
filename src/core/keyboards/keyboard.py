from aiogram.types import ReplyKeyboardMarkup


class Keyboard:
    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls)
        obj._raw = ReplyKeyboardMarkup(resize_keyboard=True)
        return obj

    def add_row(self, *buttons: str):
        self._raw.row(*buttons)

    def adapt(self) -> ReplyKeyboardMarkup:
        return self._raw
