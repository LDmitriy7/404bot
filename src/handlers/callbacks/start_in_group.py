from core import UpdateContext


async def start_in_group(ctx: UpdateContext):
    await ctx.send_message('Test in group')
