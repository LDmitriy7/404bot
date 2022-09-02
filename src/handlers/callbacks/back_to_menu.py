from core import UpdateContext
from .start import start
from assets import texts, kbs


async def back_to_menu(ctx: UpdateContext):
    await ctx.send_message(texts.you_returned_to_menu, kbs.remove)
    await start(ctx)
