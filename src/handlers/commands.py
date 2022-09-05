from core import Handler, HandlerGroup
from . import events, callbacks

COMMAND_HANDLERS = HandlerGroup(
    Handler(events.commands.start, callbacks.start),
    Handler(events.commands.get_avatars, callbacks.give_anime_avatar),
    Handler(events.commands.get_paired, callbacks.give_paired_avatars),
    Handler(events.commands.get_cute, callbacks.give_cute_picture),
    Handler(events.commands.get_angry, callbacks.give_angry_picture),
    # Handler(events.commands.send_picture, callbacks.),
)
