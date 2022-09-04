from core import Handler, HandlerGroup
from . import events, callbacks

TEXT_TRIGGER_HANDLERS = HandlerGroup(
    Handler(events.text_contain.anime_avatars, callbacks.send_anime_avatar),
    Handler(events.text_contain.paired_avatars, callbacks.send_paired_avatars),
    Handler(events.text_contain.cute_pictures, callbacks.send_cute_picture),
    Handler(events.text_contain.angry_pictures, callbacks.send_angry_picture),
)
