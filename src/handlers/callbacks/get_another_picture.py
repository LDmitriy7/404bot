from core import UpdateContext
from database import Database
from .send_anime_avatar import send_anime_avatar


async def get_another_picture(ctx: UpdateContext, db: Database):
    await send_anime_avatar(ctx, db)
