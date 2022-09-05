from core import events

anime_avatar = events.TextContainsWord(['аватарку', 'ава', 'аватарка', 'аву'])
paired_avatars = events.TextContainsWord(['авы', 'парные', 'аватарки'])
cute_picture = events.TextContainsWord(['милую'])
angry_picture = events.TextContainsWord(['агрессивную'])
