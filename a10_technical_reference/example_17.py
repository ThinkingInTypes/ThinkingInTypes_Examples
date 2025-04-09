# example_17.py
from typing import TypedDict, Required, NotRequired


class Movie(TypedDict, total=False):
    title: Required[str]  # must have title
    year: NotRequired[int]  # may omit year
