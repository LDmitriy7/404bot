from assets import Storage, PictureCategories, texts, kbs
from core import UpdateContext, Callback
from .send_picture import send_anime_avatar, send_paired_avatars, send_cute_picture, send_angry_picture
from .start import start


def give_another_picture(ctx: UpdateContext):
    storage: Storage = ctx.storage

    senders = {
        PictureCategories.ANIME_AVATARS: send_anime_avatar,
        PictureCategories.PAIRED_AVATARS: send_paired_avatars,
        PictureCategories.CUTE_PICTURES: send_cute_picture,
        PictureCategories.ANGRY_PICTURES: send_angry_picture,
    }

    sender: Callback = senders[storage.pictures_category]
    return sender(ctx)


async def back_to_menu(ctx: UpdateContext):
    await ctx.send_message(texts.you_returned_to_menu, kbs.remove)
    await start(ctx)
