# direct_value_names.py
from enum import Enum


class Status(Enum):
    OK = 1
    ERROR = 2


OK = Status.OK
ERROR = Status.ERROR

# Programmatically:
globals().update(Status.__members__)

s: Status = OK
s = ERROR
