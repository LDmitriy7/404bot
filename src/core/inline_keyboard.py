from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove


class CallbackButton:
    def __init__(self, text: str, data: str = None):
        self.text = text
        self.data = data or text

    def adapt(self) -> InlineKeyboardButton:
        return InlineKeyboardButton(self.text, callback_data=self.data)


class UrlButton:
    def __init__(self, text: str, url: str):
        self._text = text
        self._url = url

    def adapt(self) -> InlineKeyboardButton:
        return InlineKeyboardButton(self._text, url=self._url)


class InlineKeyboard:
    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls)
        obj._raw = InlineKeyboardMarkup()
        return obj

    def add_row(self, *buttons: CallbackButton | UrlButton):
        raw_buttons = [button.adapt() for button in buttons]
        self._raw.row(*raw_buttons)

    def adapt(self) -> InlineKeyboardMarkup:
        return self._raw


class Keyboard:
    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls)
        obj._raw = ReplyKeyboardMarkup(resize_keyboard=True)
        return obj

    def add_row(self, *buttons: str):
        self._raw.row(*buttons)

    def adapt(self) -> ReplyKeyboardMarkup:
        return self._raw


class RemoveKeyboard:
    _raw = ReplyKeyboardRemove()

    def adapt(self) -> ReplyKeyboardRemove:
        return self._raw
