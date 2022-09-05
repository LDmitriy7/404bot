import mongoengine as me

from core import Model


class Picture(Model):
    category: str = me.StringField()
    file_ids: list[str] = me.ListField(me.StringField())
