from core.keyboards import InlineKeyboard, UrlButton, CallbackButton, Keyboard, RemovedKeyboard
from .constants import PictureCategories


class MainMenu(InlineKeyboard):
    anime_avatars = CallbackButton("⛩ Аниме авы")
    paired_avatars = CallbackButton("🎎 Парные аватарки")
    cute_pictures = CallbackButton("💖 Милые пикчи")
    angry_pictures = CallbackButton("😡 Агрессивные")

    def __init__(self, bot_username: str):
        start_group_url = f'https://t.me/{bot_username}?startgroup=0'
        add_to_chat = UrlButton('💬 Добавить в чат', start_group_url)

        self.add_row(add_to_chat)
        self.add_row(self.anime_avatars, self.paired_avatars)
        self.add_row(self.cute_pictures, self.angry_pictures)


class PictureMenu(Keyboard):
    get_another = '♻️ Хочу другую'
    get_others = '♻️ Хочу другие'
    back_to_menu = '🔙 Меню'

    def __init__(self, picture_category: str):
        if picture_category == PictureCategories.PAIRED_AVATARS:
            get_another = self.get_others
        else:
            get_another = self.get_another

        self.add_row(get_another, self.back_to_menu)


removed = RemovedKeyboard()
