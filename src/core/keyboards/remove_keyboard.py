from aiogram.types import ReplyKeyboardRemove


class RemoveKeyboard:
    _raw = ReplyKeyboardRemove()

    def adapt(self) -> ReplyKeyboardRemove:
        return self._raw
