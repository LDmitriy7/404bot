import mongoengine as me

from . import models


class Database:
    def __init__(self, name: str):
        me.connect(name)

    @property
    def anime_avatars(self) -> list[str]:
        return [i.file_id for i in models.AnimeAvatar.find_all()]
