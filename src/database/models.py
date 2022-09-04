import mongoengine as me

from core import Model


class AnimeAvatar(Model):
    file_id: str = me.StringField()


class PairedAvatars(Model):
    file_ids: list[str] = me.ListField(me.StringField())


class CutePicture(Model):
    file_id: str = me.StringField()


class AngryPicture(Model):
    file_id: str = me.StringField()
