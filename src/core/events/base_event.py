from abc import ABC, abstractmethod

from aiogram import Dispatcher


class BaseEvent(ABC):

    @abstractmethod
    def adapt(self, dp: Dispatcher):
        """ Return aiogram decorator """
