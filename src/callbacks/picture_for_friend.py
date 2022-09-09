from assets import kbs, texts, StartParams, StartModes
from core import UpdateContext, make_start_link
from loader import db


def give_start_link(ctx: UpdateContext):
    if ctx.chat.type == 'private':
        return ctx.send_message('Эта команда работает только в группах')
    return send_start_link(ctx)


async def send_start_link(ctx: UpdateContext):
    url = make_start_url(ctx)
    keyboard = kbs.Link('Продолжить', url)
    await ctx.send_message(texts.picture_for_friend.guide, keyboard)


def make_start_url(ctx: UpdateContext) -> str:
    params = StartParams()
    params.mode = StartModes.PICTURE_FOR_FRIEND
    params.target_chat_id = ctx.chat.id
    return make_start_link(ctx.me, db, params)


async def give_menu(ctx: UpdateContext):
    await ctx.send_message('...')
