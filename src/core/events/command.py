from dataclasses import dataclass

from aiogram import Dispatcher

from .base_event import BaseEvent


@dataclass
class Command(BaseEvent):
    value: str
    chat_type: str | list[str] = None
    user_id: int | list[int] = None

    def adapt(self, dp: Dispatcher):
        return dp.message_handler(commands=self.value, chat_type=self.chat_type, user_id=self.user_id)
