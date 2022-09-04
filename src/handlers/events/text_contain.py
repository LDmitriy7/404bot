from core import events

anime_avatars = events.TextContainsWord(['аватарку', 'ава', 'аватарка', 'аву'])
paired_avatars = events.TextContainsWord(['авы', 'парные', 'аватарки'])
cute_pictures = events.TextContainsWord(['милую'])
angry_pictures = events.TextContainsWord(['агрессивную'])
