import mongoengine as me

from .model import Model


class BaseDatabase:
    def __init__(self, name: str):
        me.connect(name)

    @staticmethod
    def get_chat_data(chat_id: int) -> dict:
        if doc := ChatData.find(chat_id=chat_id):
            return doc.value
        return {}

    @staticmethod
    def set_chat_data(chat_id: int, data: dict):
        ChatData(chat_id=chat_id, value=data).save()


class ChatData(Model):
    chat_id: int = me.IntField(primary_key=True)
    value: dict = me.DictField()
