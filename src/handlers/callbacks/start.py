from assets import texts, kbs
from core import UpdateContext


def start(ctx: UpdateContext):
    if ctx.chat.type == 'private':
        return default_start(ctx)
    return group_start(ctx)


async def default_start(ctx: UpdateContext):
    user_mention = ctx.user.get_mention()
    text = texts.greeting.format(user_mention=user_mention)
    keyboard = kbs.MainMenu(ctx.me.username)
    await ctx.send_message(text, keyboard)


async def group_start(ctx: UpdateContext):
    await ctx.send_message(texts.group_greeting)
