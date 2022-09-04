from core import Handler
from . import events, callbacks

COMMAND_HANDLERS = [
    Handler(events.commands.group_start, callbacks.group_start),
    Handler(events.commands.start, callbacks.start),
    Handler(events.commands.get_avatars, callbacks.send_anime_avatar),
    Handler(events.commands.get_paired, callbacks.send_paired_avatars),
    Handler(events.commands.get_cute, callbacks.send_cute_picture),
    Handler(events.commands.get_angry, callbacks.send_angry_picture),
    Handler(events.commands.test, callbacks.test),
]

TEXT_HANDLERS = [
    Handler(events.text_triggers.anime_avatars, callbacks.send_anime_avatar),
    Handler(events.text_triggers.paired_avatars, callbacks.send_paired_avatars),
    Handler(events.text_triggers.cute_pictures, callbacks.send_cute_picture),
    Handler(events.text_triggers.angry_pictures, callbacks.send_angry_picture),
]

MAIN_MENU_HANDLERS = [
    Handler(events.main_menu.anime_avatars, callbacks.main_menu.give_anime_avatar),
    Handler(events.main_menu.paired_avatars, callbacks.main_menu.give_paired_avatars),
    Handler(events.main_menu.cute_pictures, callbacks.main_menu.give_cute_picture),
    Handler(events.main_menu.angry_pictures, callbacks.main_menu.give_angry_picture),
]

PICTURE_MENU_HANDLERS = [
    Handler(events.picture_menu.back_to_menu, callbacks.picture_menu.back_to_menu),
    Handler(events.picture_menu.get_another, callbacks.picture_menu.give_another_picture),
]

ALL_HANDLERS = COMMAND_HANDLERS + MAIN_MENU_HANDLERS + TEXT_HANDLERS + PICTURE_MENU_HANDLERS
