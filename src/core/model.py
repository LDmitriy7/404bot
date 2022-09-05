import json
import typing

import mongoengine as me

ModelT = typing.TypeVar('ModelT', bound=me.Document)


class Model(me.Document):
    meta = {
        'abstract': True,
    }

    @classmethod
    def find(cls: type[ModelT], *args, **kwargs) -> ModelT | None:
        return cls.objects(*args, **kwargs).first()

    @classmethod
    def find_all(cls: type[ModelT], *args, **kwargs) -> list[ModelT]:
        return list(cls.objects(*args, **kwargs))

    def to_dict(self) -> dict:
        return json.loads(self.to_json())
