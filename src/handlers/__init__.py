from core import HandlerGroup
from .default import DEFAULT_HANDLERS
from .send_picture import SEND_PICTURE_HANDLERS

HANDLERS = HandlerGroup(
    DEFAULT_HANDLERS,
    SEND_PICTURE_HANDLERS,
)
