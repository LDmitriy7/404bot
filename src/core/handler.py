from dataclasses import dataclass
from typing import Callable, Coroutine

from .database import BaseDatabase
from .events import BaseEvent
from .update_context import UpdateContext
from .user_data import BaseUserData

Callback1 = Callable[[UpdateContext], Coroutine]
Callback2 = Callable[[UpdateContext, BaseDatabase], Coroutine]
Callback3 = Callable[[UpdateContext, BaseUserData], Coroutine]
Callback4 = Callable[[UpdateContext, BaseDatabase, BaseUserData], Coroutine]
Callback5 = Callable[[UpdateContext, BaseUserData, BaseDatabase], Coroutine]

Callback = Callback1 | Callback2 | Callback3 | Callback4 | Callback5


@dataclass
class Handler:
    event: BaseEvent
    callback: Callback
