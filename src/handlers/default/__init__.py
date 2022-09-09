from core import HandlerGroup
from .commands import COMMANDS_GROUP
from .main_menu import MAIN_MENU_GROUP
from .picture_menu import PICTURE_MENU_GROUP
from .text_triggers import TEXT_TRIGGERS_GROUP

DEFAULT_GROUP = HandlerGroup(
    COMMANDS_GROUP,
    MAIN_MENU_GROUP,
    PICTURE_MENU_GROUP,
    TEXT_TRIGGERS_GROUP,
)
