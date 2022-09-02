from core import UpdateContext, get_random
from database import Database


async def send_anime_avatar(ctx: UpdateContext, db: Database):
    photo = get_random(db.anime_avatars)
    await ctx.send_photo(photo)
