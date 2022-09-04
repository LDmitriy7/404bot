from assets import texts, kbs, Storage, PictureCategories
from core import UpdateContext, Callback
from .send_picture import send_anime_avatar, send_paired_avatars, send_cute_picture, send_angry_picture


class PrivateChatData:
    pictures_category: str


async def give_picture(ctx: UpdateContext, chat_data: PrivateChatData, category: str):
    chat_data.pictures_category = category

    senders = {
        PictureCategories.ANIME_AVATARS: send_anime_avatar,
        PictureCategories.PAIRED_AVATARS: send_paired_avatars,
        PictureCategories.CUTE_PICTURES: send_cute_picture,
        PictureCategories.ANGRY_PICTURES: send_angry_picture,
    }

    sender: Callback = senders[category]

    if category == PictureCategories.PAIRED_AVATARS:
        keyboard = kbs.PictureMenu(plural_word_forms=True)
    else:
        keyboard = kbs.PictureMenu()

    await ctx.delete_message()
    await sender(ctx)
    await ctx.send_message(texts.picture_menu_hint, keyboard)


def give_anime_avatar(ctx: UpdateContext, chat_data: ChatData):
    return give_picture(ctx, chat_data, PictureCategories.ANIME_AVATARS)


def give_paired_avatars(ctx: UpdateContext, storage: Storage):
    return give_picture(ctx, storage, PictureCategories.PAIRED_AVATARS)


def give_cute_picture(ctx: UpdateContext, storage: Storage):
    return give_picture(ctx, storage, PictureCategories.CUTE_PICTURES)


def give_angry_picture(ctx: UpdateContext, storage: Storage):
    return give_picture(ctx, storage, PictureCategories.ANGRY_PICTURES)
