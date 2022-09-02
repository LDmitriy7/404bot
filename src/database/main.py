import mongoengine as me

from core import BaseDatabase
from . import models


class Database(BaseDatabase):
    def __init__(self, name: str):
        me.connect(name)

    @property
    def anime_avatars(self) -> list[str]:
        return [i.file_id for i in models.AnimeAvatar.find_all()]

