from assets.commands import USER_COMMANDS
from loader import bot


async def setup_chat_commands():  # TODO
    await bot.set_my_commands(USER_COMMANDS)
