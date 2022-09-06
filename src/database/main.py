from core import BaseDatabase
from .models import Picture


class Database(BaseDatabase):

    @staticmethod
    def get_pictures(category: str) -> list[Picture]:
        return Picture.find_all(category=category)

    @staticmethod
    def add_picture(category: str, file_ids: list[str]):
        Picture(category=category, file_ids=file_ids).save()
