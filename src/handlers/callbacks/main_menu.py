# from assets import texts, kbs, ChatData, PictureCategories
# from core import UpdateContext, Callback
#
#
# async def give_picture(ctx: UpdateContext, chat_data: ChatData, category: str):
#     chat_data.pictures_category = category
#
#     senders = {
#         PictureCategories.ANIME_AVATAR: send_anime_avatar,
#         PictureCategories.PAIRED_AVATARS: send_paired_avatars,
#         PictureCategories.CUTE_PICTURE: send_cute_picture,
#         PictureCategories.ANGRY_PICTURE: send_angry_picture,
#     }
#
#     sender: Callback = senders[category]
#
#     if category == PictureCategories.PAIRED_AVATARS:  # TODO: move to keyboard
#         keyboard = kbs.PictureMenu(plural_word_forms=True)
#     else:
#         keyboard = kbs.PictureMenu()
#
#     await ctx.delete_message()
#     await sender(ctx)
#     await ctx.send_message(texts.picture_menu_hint, keyboard)
#
#
# def give_anime_avatar(ctx: UpdateContext, chat_data: ChatData):
#     return give_picture(ctx, chat_data, PictureCategories.ANIME_AVATAR)
#
#
# def give_paired_avatars(ctx: UpdateContext, chat_data: ChatData):
#     return give_picture(ctx, chat_data, PictureCategories.PAIRED_AVATARS)
#
#
# def give_cute_picture(ctx: UpdateContext, chat_data: ChatData):
#     return give_picture(ctx, chat_data, PictureCategories.CUTE_PICTURE)
#
#
# def give_angry_picture(ctx: UpdateContext, chat_data: ChatData):
#     return give_picture(ctx, chat_data, PictureCategories.ANGRY_PICTURE)
