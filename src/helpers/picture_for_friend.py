from assets import ChatData, texts, kbs, StartParams, Storage, Scenes
from core import UpdateContext


async def enter_scene(storage: Storage, params: StartParams):
    storage.scene = Scenes.SEND_PICTURE
    storage.target_chat_id = params.target_chat_id


async def ask_name(ctx: UpdateContext):
    await ctx.send_message(texts.picture_for_friend.ask_user_name)


async def send_menu(ctx: UpdateContext, chat_data: ChatData):
    chat_data.target_user_name = ctx.text
    chat_data.mode = None
    await ctx.send_message(texts.picture_for_friend.ask_category, kbs.picture_for_friend_categories)
