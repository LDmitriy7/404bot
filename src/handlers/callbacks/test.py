from core import UpdateContext
from database.models import AnimeAvatar


async def test(ctx: UpdateContext):
    anime_avatars = [
        'https://telegra.ph/file/e62d42a6c1c8b2aa9b019.jpg',
        'https://telegra.ph/file/38155954f1b1e04a554f3.jpg',
    ]

    for i in anime_avatars:
        AnimeAvatar(file_id=i)

    await ctx.send_message('ok')
