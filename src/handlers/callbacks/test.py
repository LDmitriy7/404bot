from assets import ChatData
from core import UpdateContext


async def test(ctx: UpdateContext):
    chat_data: ChatData = ctx.chat_data
    counter = (ctx.chat_data.counter or 0) + 1
    ctx.chat_data.counter = counter
    await ctx.send_message(f'Messages count: {counter}')
