import helpers
from assets import PictureCategories, kbs, texts, ChatData
from core import UpdateContext


def give_anime_avatar(ctx: UpdateContext, chat_data: ChatData):
    return give_picture(ctx, chat_data, PictureCategories.ANIME_AVATAR)


def give_paired_avatars(ctx: UpdateContext, chat_data: ChatData):
    return give_picture(ctx, chat_data, PictureCategories.PAIRED_AVATARS)


def give_cute_picture(ctx: UpdateContext, chat_data: ChatData):
    return give_picture(ctx, chat_data, PictureCategories.CUTE_PICTURE)


def give_angry_picture(ctx: UpdateContext, chat_data: ChatData):
    return give_picture(ctx, chat_data, PictureCategories.ANGRY_PICTURE)


async def give_picture(ctx: UpdateContext, chat_data: ChatData, category: str):
    chat_data.picture_category = category
    await ctx.delete_message()
    await helpers.give_picture(ctx, category)
    await send_picture_menu(ctx, category)


def send_picture_menu(ctx: UpdateContext, picture_category: str):
    keyboard = kbs.PictureMenu(picture_category)
    return ctx.send_message(texts.picture_menu_hint, keyboard)
