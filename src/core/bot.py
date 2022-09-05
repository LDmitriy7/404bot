from aiogram import Bot as RawBot
from aiogram import types


class Bot:
    def __init__(self, token: str):
        self._raw = RawBot(token, parse_mode='html')

    async def set_my_commands(self, commands: list[types.BotCommand]):
        await self._raw.set_my_commands(commands)
