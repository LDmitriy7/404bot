from core import UpdateContext
from ..assets import texts, kbs


async def start(ctx: UpdateContext):
    user_mention = ctx.user.get_mention()
    text = texts.greeting.format(user_mention=user_mention)
    keyboard = kbs.Menu(ctx.me.username)
    await ctx.send_message(text, keyboard)
