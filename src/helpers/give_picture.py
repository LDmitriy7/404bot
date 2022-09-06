from core import UpdateContext, get_random
from database.models import Picture
from loader import db


async def give_picture(ctx: UpdateContext, category: str):
    await send_random_picture(ctx, category)


def send_random_picture(ctx: UpdateContext, category: str):
    pictures = db.get_pictures(category)
    picture = get_random(pictures)
    return send_picture(ctx, picture)


def send_picture(ctx: UpdateContext, picture: Picture):
    if len(picture.file_ids) == 1:
        return ctx.send_photo(picture.file_ids[0])
    else:
        return ctx.send_media_group(picture.file_ids)
