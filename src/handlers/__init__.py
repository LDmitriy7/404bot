from core import Handler
from . import events, callbacks

COMMAND_HANDLERS = [
    Handler(events.commands.start_in_group, callbacks.start_in_group),
    Handler(events.commands.start, callbacks.start),
    Handler(events.commands.test, callbacks.test),
]

MAIN_MENU_HANDLERS = [
    Handler(events.main_menu.anime_avatars, callbacks.main_menu.give_anime_avatar),
]

PICTURE_MENU_HANDLERS = [
    Handler(events.picture_menu.back_to_menu, callbacks.back_to_menu),
    Handler(events.picture_menu.get_another, callbacks.picture_menu.give_another_picture),
]

ALL_HANDLERS = COMMAND_HANDLERS + MAIN_MENU_HANDLERS + PICTURE_MENU_HANDLERS
