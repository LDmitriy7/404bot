import callbacks as actions
import events.commands as on
from core import Handler, HandlerGroup

ON_COMMAND = HandlerGroup(
    Handler(on.start, actions.start),
    Handler(on.get_avatars, actions.give_anime_avatar),
    Handler(on.get_paired, actions.give_paired_avatars),
    Handler(on.get_cute, actions.give_cute_picture),
    Handler(on.get_angry, actions.give_angry_picture),
    Handler(on.send_picture, actions.picture_for_friend.give_start_link),
    Handler(on.test, actions.test),
)
