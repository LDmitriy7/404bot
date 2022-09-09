import config
from assets import commands
from core import events

start = events.Command(commands.START)
get_avatars = events.Command(commands.GET_AVATARS)
get_paired = events.Command(commands.GET_PAIRED)
get_cute = events.Command(commands.GET_CUTE)
get_angry = events.Command(commands.GET_ANGRY)
test = events.Command(commands.TEST, user_id=config.ADMINS_IDS)
send_picture = events.Command(commands.SEND_PICTURE)
