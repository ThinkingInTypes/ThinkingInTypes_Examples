# all_combinations.py
# pyright: reportArgumentType=false
from enum import Flag, EnumCheck, auto


class AllFlags(Flag, boundary=EnumCheck.NAMED_FLAGS):
    FIRST = auto()  # 1
    SECOND = auto()  # 2
    THIRD = auto()  # 4
    ALL = FIRST | SECOND | THIRD  # 7


# NAMED_FLAGS not implemented yet
class Missing(Flag, boundary=EnumCheck.NAMED_FLAGS):
    FIRST = auto()
    SECOND = auto()
    THIRD = auto()
