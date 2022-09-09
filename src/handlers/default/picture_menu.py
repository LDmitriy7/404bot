import actions.picture_menu as actions
import events.picture_menu as events
from core import Handler, HandlerGroup

PICTURE_MENU_GROUP = HandlerGroup(
    Handler(events.back_to_menu, actions.back_to_menu),
    Handler(events.get_another, actions.give_another_picture),
)
