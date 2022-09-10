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

    @staticmethod
    def get_storage_data(chat_id: int, user_id: int) -> dict:
        key = StorageKey(chat_id=chat_id, user_id=user_id)
        if doc := Storage.find(key=key):
            return doc.data
        return {}

    @staticmethod
    def set_storage_data(chat_id: int, user_id: int, data: dict):
        key = StorageKey(chat_id=chat_id, user_id=user_id)
        Storage(key=key, data=data).save()


class ChatData(Model):
    chat_id: int = me.IntField(primary_key=True)
    value: dict = me.DictField()


class StartParams(Model):
    data: dict = me.DictField()


class StorageKey(me.EmbeddedDocument):
    chat_id: int = me.IntField()
    user_id: int = me.IntField()


class Storage(Model):
    key: StorageKey = me.EmbeddedDocumentField(StorageKey, primary_key=True)
    data: dict = me.DictField()
