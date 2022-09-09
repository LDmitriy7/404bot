from assets import ChatData, texts, StartParams, kbs
from core import UpdateContext


async def ask_user_name(ctx: UpdateContext, params: StartParams, chat_data: ChatData):
    chat_data.target_chat_id = params.target_chat_id
    chat_data.mode = params.mode
    await ctx.send_message(texts.picture_for_friend.ask_user_name)


async def send_menu(ctx: UpdateContext, chat_data: ChatData):
    chat_data.target_user_name = ctx.text
    chat_data.mode = None
    await ctx.send_message(texts.picture_for_friend.ask_category, kbs.picture_for_friend_categories)
