from core import UpdateContext
from database import Database
import helpers
from assets import texts, kbs, PictureCategories, UserData


async def give_anime_avatar(ctx: UpdateContext, db: Database, user_data: UserData):
    user_data.pictures_category = PictureCategories.ANIME_AVATARS
    await ctx.delete_message()
    await helpers.send_anime_avatar(ctx, db)
    await ctx.send_message(texts.picture_menu_hint, kbs.picture_menu)
