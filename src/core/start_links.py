from aiogram.types import User

from .database import BaseDatabase
from .start_params import BaseStartParams


def make_start_link(bot: User, db: BaseDatabase, params: BaseStartParams):
    params_id = db.save_start_params(params.__data__)
    return f'https://t.me/{bot.username}?start={params_id}'
