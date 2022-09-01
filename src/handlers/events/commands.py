from core import events

start = events.Command('start')
start_in_group = events.Command('start', chat_type=['group', 'supergroup'])
