from core import HandlerGroup
from .commands import COMMAND_HANDLERS
from .for_admins import ADMIN_HANDLERS
# from .main_menu import MAIN_MENU_HANDLERS
# from .picture_menu import PICTURE_MENU_HANDLERS
from .text_triggers import TEXT_TRIGGER_HANDLERS

HANDLERS = HandlerGroup(
    ADMIN_HANDLERS,
    TEXT_TRIGGER_HANDLERS,
    COMMAND_HANDLERS,
    # MAIN_MENU_HANDLERS,
    # PICTURE_MENU_HANDLERS,
)
