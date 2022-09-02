from core import UpdateContext, get_random
from database import Database
from ..assets import texts, kbs


async def send_anime_avatar(ctx: UpdateContext, db: Database):
    photo = get_random(db.anime_avatars)
    await ctx.send_photo(photo)


async def send_anime_avatar_from_menu(ctx: UpdateContext, db: Database):
    await ctx.delete_message()
    await send_anime_avatar(ctx, db)
    await ctx.send_message(texts.picture_menu_hint, kbs.picture_menu)
