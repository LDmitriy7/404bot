from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


class CallbackButton:
    def __init__(self, text: str, data: str = None):
        self._text = text
        self._data = data or text

    def adapt(self) -> InlineKeyboardButton:
        return InlineKeyboardButton(self._text, callback_data=self._data)


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
