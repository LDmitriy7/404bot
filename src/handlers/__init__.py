from core import HandlerGroup
from .commands import COMMAND_HANDLERS
from .main_menu import MAIN_MENU_HANDLERS
from .picture_menu import PICTURE_MENU_HANDLERS
from .text_triggers import TEXT_TRIGGER_HANDLERS

HANDLERS = HandlerGroup(
    COMMAND_HANDLERS,
    MAIN_MENU_HANDLERS,
    PICTURE_MENU_HANDLERS,
    TEXT_TRIGGER_HANDLERS,
)
