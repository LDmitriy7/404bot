from core import HandlerGroup
from .commands import COMMAND_GROUP
from .main_menu import MAIN_MENU_GROUP
from .picture_menu import PICTURE_MENU_GROUP
from .text_triggers import TEXT_TRIGGER_GROUP

DEFAULT_GROUP = HandlerGroup(
    COMMAND_GROUP,
    MAIN_MENU_GROUP,
    PICTURE_MENU_GROUP,
    TEXT_TRIGGER_GROUP,
)
