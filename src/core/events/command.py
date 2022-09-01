from dataclasses import dataclass

from .base_event import BaseEvent


@dataclass
class Command(BaseEvent):
    value: str
    chat_type: str | list[str] = None
