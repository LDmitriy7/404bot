import mongoengine as me
from aiogram.contrib.fsm_storage.mongo import MongoStorage

from core import BaseDatabase
from .models import Picture


class Database(BaseDatabase):
    def __init__(self, name: str):
        self.storage = MongoStorage(db_name=name)
        me.connect(name)

    @staticmethod
    def get_pictures(category: str) -> list[Picture]:
        return Picture.find_all(category=category)

    @staticmethod
    def add_picture(category: str, file_ids: list[str]):
        Picture(category=category, file_ids=file_ids).save()
