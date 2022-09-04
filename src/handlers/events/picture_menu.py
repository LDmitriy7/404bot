from assets import kbs
from core import events

back_to_menu = events.Text(kbs.PictureMenu.back_to_menu)
get_another = events.Text([kbs.PictureMenu.get_another, kbs.PictureMenu.get_others])
