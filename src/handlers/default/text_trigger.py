import callbacks as actions
import events.hears_word as on
from core import Handler, HandlerGroup

ON_TEXT_TRIGGER = HandlerGroup(
    Handler(on.anime_avatar, actions.give_anime_avatar),
    Handler(on.paired_avatars, actions.give_paired_avatars),
    Handler(on.cute_picture, actions.give_cute_picture),
    Handler(on.angry_picture, actions.give_angry_picture),
)
