DATA_KEY = '__data__'


class BaseChatData:
    def __init__(self, data: dict):
        self.__dict__[DATA_KEY] = {}
        self.__data__: dict
        self.__data__.update(data)

    def __getattr__(self, item: str):
        if item == DATA_KEY:
            return self.__dict__[DATA_KEY]
        return self.__data__.get(item)

    def __setattr__(self, item: str, value):
        self.__data__[item] = value
