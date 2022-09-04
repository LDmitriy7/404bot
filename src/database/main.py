import mongoengine as me
from aiogram.contrib.fsm_storage.mongo import MongoStorage

from core import BaseDatabase
from . import models


class Database(BaseDatabase):
    def __init__(self, name: str):
        self.storage = MongoStorage(db_name=name)
        me.connect(name)

    @property
    def anime_avatars(self) -> list[str]:
        return [i.file_id for i in models.AnimeAvatar.find_all()]

    @property
    def paired_avatars(self) -> list[list[str]]:
        return [i.file_ids for i in models.PairedAvatars.find_all()]

    @property
    def cute_pictures(self) -> list[str]:
        return [i.file_id for i in models.CutePicture.find_all()]

    @property
    def angry_pictures(self) -> list[str]:
        return [i.file_id for i in models.AngryPicture.find_all()]
