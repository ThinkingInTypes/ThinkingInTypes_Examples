# continuous_values.py
# pyright: reportArgumentType=false
from enum import Enum, EnumCheck


class Status(Enum, boundary=EnumCheck.CONTINUOUS):
    OK = 1
    WARNING = 2
    ERROR = 3
    MISSING = 5  # error: gap (not implemented yet)
