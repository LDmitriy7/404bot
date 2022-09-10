import actions
import events.hears_word as events
from core import Handler, HandlerGroup

TEXT_TRIGGER_GROUP = HandlerGroup(
    Handler(events.anime_avatar, actions.give_anime_avatar),
    Handler(events.paired_avatars, actions.give_paired_avatars),
    Handler(events.cute_picture, actions.give_cute_picture),
    Handler(events.angry_picture, actions.give_angry_picture),
)
