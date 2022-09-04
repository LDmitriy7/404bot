from __future__ import annotations

from .handler import Handler


class HandlerGroup:
    def __init__(self, *handlers: Handler | HandlerGroup):
        self._handlers = handlers

    def __iter__(self):
        for item in self._handlers:
            if isinstance(item, HandlerGroup):
                yield from iter(item)
            else:
                yield item
