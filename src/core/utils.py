import random
from typing import TypeVar

T = TypeVar('T')


def get_random(items: list[T]) -> T:
    return random.choice(items)


def listify(item: T | list[T]) -> list[T]:
    if isinstance(item, list):
        return item
    return [item]
