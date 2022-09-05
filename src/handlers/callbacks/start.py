import config
from assets import texts, kbs
from core import UpdateContext
from helpers import setup_chat_commands


async def start(ctx: UpdateContext):
    if ctx.user.id in config.ADMINS_IDS:
        await setup_chat_commands()
    if ctx.chat.type == 'private':
        await default_start(ctx)
    else:
        await group_start(ctx)


async def default_start(ctx: UpdateContext):
    user_mention = ctx.user.get_mention()
    text = texts.greeting.format(user_mention=user_mention)
    keyboard = kbs.MainMenu(ctx.me.username)
    await ctx.send_message(text, keyboard)


async def group_start(ctx: UpdateContext):
    await ctx.send_message(texts.group_greeting)
