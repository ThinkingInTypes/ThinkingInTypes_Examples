# return_self.py
from typing import Self


class Form:
    def set_title(self, title: str) -> Self:
        self.title = title
        return self
