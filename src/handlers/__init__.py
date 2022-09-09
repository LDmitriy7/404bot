from core import HandlerGroup
from .default import DEFAULT_GROUP
from .send_picture import SEND_PICTURE_GROUP

HANDLERS = HandlerGroup(
    DEFAULT_GROUP,
    SEND_PICTURE_GROUP,
)
