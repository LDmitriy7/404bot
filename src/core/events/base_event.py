from abc import ABC, abstractmethod
from typing import Callable

from aiogram import Dispatcher

Decorator = Callable[[Callable], None]


class BaseEvent(ABC):

    @abstractmethod
    def adapt(self, dp: Dispatcher) -> Decorator:
        """ Return aiogram decorator """
