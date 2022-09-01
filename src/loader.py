import config
from core import App
from handlers import HANDLERS

app = App(config.BOT_TOKEN, HANDLERS)
