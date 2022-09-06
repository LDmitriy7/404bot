import config
from core import App, Bot
from database import Database

db = Database(config.MONGO_DB)
bot = Bot(config.BOT_TOKEN)
app = App(bot, db)
