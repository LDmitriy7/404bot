from dataclasses import dataclass
from typing import Callable, Coroutine

from .events import BaseEvent
from .update_context import UpdateContext

# TODO
Callback = Callable[[UpdateContext], Coroutine] | Callable[[UpdateContext, ...], Coroutine]


@dataclass
class Handler:
    event: BaseEvent
    callback: Callback
