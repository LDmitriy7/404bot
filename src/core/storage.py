DATA_KEY = '__data__'


class BaseStorage:
    scene: str
    __data__: dict

    def __init__(self, data: dict = None):
        data = data or {}
        self.__dict__[DATA_KEY] = data.copy()

    def __getattr__(self, item: str):
        if item == DATA_KEY:
            return self.__dict__[DATA_KEY]
        return self.__data__.get(item)

    def __setattr__(self, item: str, value):
        self.__data__[item] = value

    def __str__(self):
        return f'Storage({self.__data__})'
