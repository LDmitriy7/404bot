from .inline_keyboard import InlineKeyboard, CallbackButton, UrlButton
from .keyboard import Keyboard
from .remove_keyboard import RemoveKeyboard

AnyKeyboard = Keyboard | InlineKeyboard | RemoveKeyboard
