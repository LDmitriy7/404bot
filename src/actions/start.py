import config
from assets import texts, kbs, StartParams, StartModes, Storage
from core import UpdateContext
from helpers import setup_chat_commands, picture_for_friend


async def start(ctx: UpdateContext, storage: Storage, params: StartParams):
    if ctx.user.id in config.ADMINS_IDS:
        await setup_chat_commands()
    if ctx.chat.type == 'private':
        await private_start(ctx, storage, params)
    else:
        await group_start(ctx)


async def private_start(ctx: UpdateContext, storage: Storage, params: StartParams):
    if params.mode == StartModes.PICTURE_FOR_FRIEND:
        await picture_for_friend.enter_scene(storage, params)
        await picture_for_friend.ask_name(ctx)
    else:
        await default_start(ctx)


async def default_start(ctx: UpdateContext):
    user_mention = ctx.user.get_mention()
    text = texts.greeting.format(user_mention=user_mention)
    keyboard = kbs.MainMenu(ctx.me.username)
    await ctx.send_message(text, keyboard)


async def group_start(ctx: UpdateContext):
    await ctx.send_message(texts.group_greeting)
