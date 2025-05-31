# enum_str.py
from enum import StrEnum

class Status(StrEnum):
    OK = "yes!"
    ERROR = "no."
    RETRY = "again!"
