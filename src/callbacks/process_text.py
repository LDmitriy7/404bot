from assets import ChatData, StartModes
from core import UpdateContext
from helpers import picture_for_friend, ignore


def process_text(ctx: UpdateContext, chat_data: ChatData):
    if chat_data.mode == StartModes.PICTURE_FOR_FRIEND:
        return picture_for_friend.send_menu(ctx, chat_data)
    return ignore()
