from dataclasses import dataclass

from aiogram import Dispatcher, types

from .base_event import BaseEvent
from ..utils import listify


@dataclass
class Text(BaseEvent):
    value: str | list[str]
    chat_type: str | list[str] = None

    def adapt(self, dp: Dispatcher):
        return dp.message_handler(text=self.value, chat_type=self.chat_type)


@dataclass
class TextContainsWord(BaseEvent):
    value: str | list[str]
    chat_type: str | list[str] = None

    def _filter(self, msg: types.Message):
        text_words = msg.text.lower().split()
        search_words = [i.lower() for i in listify(self.value)]
        return any(x in text_words for x in search_words)

    def adapt(self, dp: Dispatcher):
        return dp.message_handler(self._filter, chat_type=self.chat_type)
