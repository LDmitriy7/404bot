from core import Handler, HandlerGroup
from . import events, callbacks

MAIN_MENU_HANDLERS = HandlerGroup(
    Handler(events.main_menu.anime_avatars, callbacks.main_menu.give_anime_avatar),
    Handler(events.main_menu.paired_avatars, callbacks.main_menu.give_paired_avatars),
    Handler(events.main_menu.cute_pictures, callbacks.main_menu.give_cute_picture),
    Handler(events.main_menu.angry_pictures, callbacks.main_menu.give_angry_picture),
)
