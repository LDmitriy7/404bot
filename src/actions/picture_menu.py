from assets import texts, kbs, ChatData
from core import UpdateContext
from helpers import give_picture
from .start import default_start


def give_another_picture(ctx: UpdateContext, chat_data: ChatData):
    return give_picture(ctx, chat_data.picture_category)


async def back_to_menu(ctx: UpdateContext):
    await ctx.send_message(texts.returned_to_main_menu, kbs.removed)
    await default_start(ctx)
