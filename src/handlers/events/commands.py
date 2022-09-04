import config
from core import events

start = events.Command('start')
group_start = events.Command('start', chat_type=['group', 'supergroup'])
test = events.Command('test', user_id=config.ADMINS_IDS)

get_avatars = events.Command('get_avatars')
get_paired = events.Command('get_paired')
get_cute = events.Command('get_cute')
get_angry = events.Command('get_angry')
