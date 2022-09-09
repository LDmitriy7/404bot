import config
from assets import texts, kbs, StartParams, StartModes, ChatData
from core import UpdateContext
from helpers import setup_chat_commands, picture_for_friend


async def start(ctx: UpdateContext, params: StartParams, chat_data: ChatData):
    if ctx.user.id in config.ADMINS_IDS:
        await setup_chat_commands()
    if ctx.chat.type == 'private':
        await private_start(ctx, params, chat_data)
    else:
        await group_start(ctx)


def private_start(ctx: UpdateContext, params: StartParams, chat_data: ChatData):
    if params.mode == StartModes.PICTURE_FOR_FRIEND:
        return picture_for_friend.ask_user_name(ctx, params, chat_data)
    return default_start(ctx)


async def default_start(ctx: UpdateContext):
    user_mention = ctx.user.get_mention()
    text = texts.greeting.format(user_mention=user_mention)
    keyboard = kbs.MainMenu(ctx.me.username)
    await ctx.send_message(text, keyboard)


async def group_start(ctx: UpdateContext):
    await ctx.send_message(texts.group_greeting)
