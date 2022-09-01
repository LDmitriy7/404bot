from core import Handler
from . import events, callbacks

HANDLERS = [
    Handler(events.commands.start_in_group, callbacks.start_in_group),
    Handler(events.commands.start, callbacks.start),
    # Handler(events.menu.anime_avatars, callbacks.send_anime_avatars),
]
