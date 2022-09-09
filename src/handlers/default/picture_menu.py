import callbacks.picture_menu as actions
import events.picture_menu as on
from core import Handler, HandlerGroup

ON_PICTURE_MENU_CLICK = HandlerGroup(
    Handler(on.back_to_menu, actions.back_to_menu),
    Handler(on.get_another, actions.give_another_picture),
)
