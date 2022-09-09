import actions
import events.commands as events
from core import Handler, HandlerGroup

GET_PICTURES_GROUP = HandlerGroup(
    Handler(events.get_avatars, actions.give_anime_avatar),
    Handler(events.get_paired, actions.give_paired_avatars),
    Handler(events.get_cute, actions.give_cute_picture),
    Handler(events.get_angry, actions.give_angry_picture),
)

COMMANDS_GROUP = HandlerGroup(
    Handler(events.start, actions.start),
    Handler(events.send_picture, actions.send_picture.give_start_link),
    Handler(events.test, actions.test),
    GET_PICTURES_GROUP,
)
