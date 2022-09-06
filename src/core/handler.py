from dataclasses import dataclass
from typing import Callable, Coroutine

from .events import BaseEvent

Callback = Callable[[...], Coroutine]


@dataclass
class Handler:
    event: BaseEvent
    callback: Callback
