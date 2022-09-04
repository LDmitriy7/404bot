from core import UpdateContext, get_random
from loader import db


async def send_anime_avatar(ctx: UpdateContext):
    photo = get_random(db.anime_avatars)
    await ctx.send_photo(photo)


async def send_paired_avatars(ctx: UpdateContext):
    photos = get_random(db.paired_avatars)
    await ctx.send_media_group(photos)


async def send_cute_picture(ctx: UpdateContext):
    photo = get_random(db.cute_pictures)
    await ctx.send_photo(photo)


async def send_angry_picture(ctx: UpdateContext):
    photo = get_random(db.angry_pictures)
    await ctx.send_photo(photo)
