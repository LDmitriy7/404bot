from core import Handler, HandlerGroup
from . import events, callbacks

TEXT_TRIGGER_HANDLERS = HandlerGroup(
    Handler(events.hears_word.anime_avatar, callbacks.give_anime_avatar),
    Handler(events.hears_word.paired_avatars, callbacks.give_paired_avatars),
    Handler(events.hears_word.cute_picture, callbacks.give_cute_picture),
    Handler(events.hears_word.angry_picture, callbacks.give_angry_picture),
)
