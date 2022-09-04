from core import Handler, HandlerGroup
from . import events, callbacks

PICTURE_MENU_HANDLERS = HandlerGroup(
    Handler(events.picture_menu.back_to_menu, callbacks.picture_menu.back_to_menu),
    Handler(events.picture_menu.get_another, callbacks.picture_menu.give_another_picture),
)
