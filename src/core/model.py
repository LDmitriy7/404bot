import json
import typing

import mongoengine as me

DocT = typing.TypeVar('DocT', bound='BaseDocument')


class Model(me.Document):
    meta = {
        'abstract': True,
    }

    @classmethod
    def find(cls: type[DocT], *args, **kwargs) -> DocT | None:
        return cls.objects(*args, **kwargs).first()

    @classmethod
    def find_all(cls: type[DocT], *args, **kwargs) -> list[DocT]:
        return list(cls.objects(*args, **kwargs))

    def to_dict(self) -> dict:
        return json.loads(self.to_json())
