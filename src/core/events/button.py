from dataclasses import dataclass

from aiogram import Dispatcher

from .base_event import BaseEvent
from ..keyboards import CallbackButton


@dataclass
class Button(BaseEvent):
    value: CallbackButton
    chat_type: str | list[str] = None

    def adapt(self, dp: Dispatcher):
        return dp.callback_query_handler(text=self.value.data, chat_type=self.chat_type)
