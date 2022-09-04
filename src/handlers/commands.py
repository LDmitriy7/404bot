from core import Handler, HandlerGroup
from . import events, callbacks

COMMAND_HANDLERS = HandlerGroup(
    Handler(events.commands.start, callbacks.start),
    Handler(events.commands.get_avatars, callbacks.send_anime_avatar),
    Handler(events.commands.get_paired, callbacks.send_paired_avatars),
    Handler(events.commands.get_cute, callbacks.send_cute_picture),
    Handler(events.commands.get_angry, callbacks.send_angry_picture),
)
