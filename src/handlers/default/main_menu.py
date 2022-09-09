import actions.main_menu as actions
import events.main_menu as events
from core import Handler, HandlerGroup

MAIN_MENU_GROUP = HandlerGroup(
    Handler(events.anime_avatars, actions.give_anime_avatar),
    Handler(events.paired_avatars, actions.give_paired_avatars),
    Handler(events.cute_pictures, actions.give_cute_picture),
    Handler(events.angry_pictures, actions.give_angry_picture),
)
