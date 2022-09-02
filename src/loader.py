import config
from core import App
from database import Database
from handlers import HANDLERS

db = Database('404bot')
app = App(config.BOT_TOKEN, HANDLERS, db)
