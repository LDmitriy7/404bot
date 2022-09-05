from assets import texts, kbs
from core import UpdateContext
from .start import start


# def give_another_picture(ctx: UpdateContext):
#     storage: Storage = ctx.storage
#
#     senders = {
#         PictureCategories.ANIME_AVATAR: send_anime_avatar,
#         PictureCategories.PAIRED_AVATARS: send_paired_avatars,
#         PictureCategories.CUTE_PICTURE: send_cute_picture,
#         PictureCategories.ANGRY_PICTURE: send_angry_picture,
#     }
#
#     sender: Callback = senders[storage.pictures_category]
#     return sender(ctx)


async def back_to_menu(ctx: UpdateContext):
    await ctx.send_message(texts.you_returned_to_menu, kbs.remove)
    await start(ctx)
