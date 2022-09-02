from core import UpdateContext
from database import Database
import helpers
from assets import PictureCategories, UserData


async def give_another_picture(ctx: UpdateContext, db: Database, user_data: UserData):
    match user_data.pictures_category:
        case PictureCategories.ANIME_AVATARS:
            await helpers.send_anime_avatar(ctx, db)
        case _:
            await ctx.send_message('Ошибка')
