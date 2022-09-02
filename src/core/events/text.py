from dataclasses import dataclass

from aiogram import Dispatcher

from .base_event import BaseEvent


@dataclass
class Text(BaseEvent):
    value: str
    chat_type: str | list[str] = None

    def adapt(self, dp: Dispatcher):
        return dp.message_handler(text=self.value, chat_type=self.chat_type)
