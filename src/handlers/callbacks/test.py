from assets import PictureCategories
from core import UpdateContext
from loader import db


def add_pictures():
    db.add_picture(PictureCategories.ANIME_AVATAR, ['https://telegra.ph/file/38155954f1b1e04a554f3.jpg'])
    db.add_picture(PictureCategories.PAIRED_AVATARS, ['https://telegra.ph/file/b7372657ce973c8c6c3bf.jpg',
                                                      'https://telegra.ph/file/f943c94b14c7b30cea290.jpg'])
    db.add_picture(PictureCategories.CUTE_PICTURE, ['https://telegra.ph/file/0dac03dfee96080a2d7ab.jpg'])
    db.add_picture(PictureCategories.ANGRY_PICTURE, ['https://telegra.ph/file/ed333fa6b8f39620c759e.jpg'])


async def test(ctx: UpdateContext):
    # add_pictures()
    await ctx.send_message('ok')
