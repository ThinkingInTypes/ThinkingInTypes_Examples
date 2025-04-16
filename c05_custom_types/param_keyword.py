# param_keyword.py
from enum import Enum


class ParamKeyword(Enum):
    MIN = "MIN"
    MAX = "MAX"
    DEF = "DEF"


ParamType = float | ParamKeyword
