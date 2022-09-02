from core import InlineKeyboard, UrlButton, CallbackButton, Keyboard, RemoveKeyboard


class Menu(InlineKeyboard):
    anime_avatars = CallbackButton("⛩ Аниме авы")
    paired_avatars = CallbackButton("🎎 Парные аватарки")
    cute_pictures = CallbackButton("💖 Милые пикчи")
    aggressive_pictures = CallbackButton("😡 Агрессивные")

    def __init__(self, bot_username: str):
        start_group_url = f'https://t.me/{bot_username}?startgroup=0'
        add_to_chat = UrlButton('💬 Добавить в чат', start_group_url)

        self.add_row(add_to_chat)
        self.add_row(self.anime_avatars, self.paired_avatars)
        self.add_row(self.cute_pictures, self.aggressive_pictures)


class PictureMenu(Keyboard):
    get_another = '♻️ Хочу другую'
    back_to_menu = '🔙 Меню'

    def __init__(self):
        self.add_row(self.get_another, self.back_to_menu)


picture_menu = PictureMenu()

remove = RemoveKeyboard()
