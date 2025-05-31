# enum_int.py
from enum import IntEnum


class Status(IntEnum):
    OK = 1
    ERROR = 2
    RETRY = 3
