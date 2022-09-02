import config
from core import App
from database import Database

db = Database('404bot')
app = App(config.BOT_TOKEN, db)
