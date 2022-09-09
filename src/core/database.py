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

    @staticmethod
    def get_start_params(params_id: str) -> dict:
        if doc := StartParams.find(id=params_id):
            return doc.data
        return {}

    @staticmethod
    def save_start_params(params: dict) -> str:
        doc = StartParams(data=params).save()
        return str(doc.id)


class ChatData(Model):
    chat_id: int = me.IntField(primary_key=True)
    value: dict = me.DictField()


class StartParams(Model):
    data: dict = me.DictField()
