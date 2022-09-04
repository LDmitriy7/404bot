from abc import ABC

from aiogram.dispatcher.storage import BaseStorage


class BaseDatabase(ABC):
    storage: BaseStorage = None
