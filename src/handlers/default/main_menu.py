import callbacks.main_menu as actions
import events.main_menu as on
from core import Handler, HandlerGroup

ON_MAIN_MENU_CLICK = HandlerGroup(
    Handler(on.anime_avatars, actions.give_anime_avatar),
    Handler(on.paired_avatars, actions.give_paired_avatars),
    Handler(on.cute_pictures, actions.give_cute_picture),
    Handler(on.angry_pictures, actions.give_angry_picture),
)
