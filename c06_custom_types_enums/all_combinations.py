# all_combinations.py
from enum import Flag, auto, verify, NAMED_FLAGS

from book_utils import Catch


@verify(NAMED_FLAGS)
class AllFlags(Flag):
    FIRST = auto()  # 1
    SECOND = auto()  # 2
    THIRD = auto()  # 4
    ALL = FIRST | SECOND | THIRD  # 7


with Catch():

    @verify(NAMED_FLAGS)
    class Missing(Flag):
        FIRST = auto()
        SECOND = auto()
        THIRD = auto()
