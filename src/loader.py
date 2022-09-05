import config
from core import App, Bot
from database import Database

db = Database('404bot')
bot = Bot(config.BOT_TOKEN)
app = App(bot, db)
