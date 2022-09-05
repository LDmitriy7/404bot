from assets import PictureCategories
from core import UpdateContext
from helpers import send_random_picture


def give_anime_avatar(ctx: UpdateContext):
    return give_picture(ctx, PictureCategories.ANIME_AVATAR)


def give_paired_avatars(ctx: UpdateContext):
    return give_picture(ctx, PictureCategories.PAIRED_AVATARS)


def give_cute_picture(ctx: UpdateContext):
    return give_picture(ctx, PictureCategories.CUTE_PICTURE)


def give_angry_picture(ctx: UpdateContext):
    return give_picture(ctx, PictureCategories.ANGRY_PICTURE)


async def give_picture(ctx: UpdateContext, category: str):
    await send_random_picture(ctx, category)
