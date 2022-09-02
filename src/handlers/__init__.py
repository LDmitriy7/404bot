from core import Handler
from . import events, callbacks

HANDLERS = [
    Handler(events.commands.start_in_group, callbacks.start_in_group),
    Handler(events.commands.start, callbacks.start),
    Handler(events.menu.anime_avatars, callbacks.send_anime_avatar_from_menu),
    Handler(events.picture_menu.back_to_menu, callbacks.back_to_menu),
    Handler(events.picture_menu.get_another, callbacks.get_another_picture),
    Handler(events.commands.test, callbacks.test),
]
