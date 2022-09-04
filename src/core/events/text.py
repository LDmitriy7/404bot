from dataclasses import dataclass

from aiogram import Dispatcher, types

from .base_event import BaseEvent


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
        search_words = self.value if isinstance(self.value, list) else [self.value]

        for s in search_words:
            if s.lower() in text_words:
                return True

        return False

    def adapt(self, dp: Dispatcher):
        return dp.message_handler(self._filter, chat_type=self.chat_type)
