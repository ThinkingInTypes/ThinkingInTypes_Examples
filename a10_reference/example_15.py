# example_15.py
from typing import Self


class MyBuilder:
    def set_name(self, name: str) -> Self:
        self.name = name  # noqa: Instance attribute
        return self
