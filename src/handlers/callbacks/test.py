from assets import ChatData
from core import UpdateContext


async def test(ctx: UpdateContext, chat_data: ChatData):
    await ctx.send_message(f'{chat_data.picture_category = }')
