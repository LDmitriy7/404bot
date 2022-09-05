from core import Handler, HandlerGroup
from . import events, callbacks

ADMIN_HANDLERS = HandlerGroup(
    Handler(events.commands.test, callbacks.test)
)
