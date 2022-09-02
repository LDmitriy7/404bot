import mongoengine as me

from core import Model


class AnimeAvatar(Model):
    file_id: str = me.StringField()
