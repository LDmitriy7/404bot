from core import HandlerGroup
from .command import ON_COMMAND
from .main_menu import ON_MAIN_MENU_CLICK
from .picture_menu import ON_PICTURE_MENU_CLICK
from .text_trigger import ON_TEXT_TRIGGER

DEFAULT_HANDLERS = HandlerGroup(
    ON_COMMAND,
    ON_MAIN_MENU_CLICK,
    ON_PICTURE_MENU_CLICK,
    ON_TEXT_TRIGGER,
)
