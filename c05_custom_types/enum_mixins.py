# enum_mixins.py
from enum import Enum

class StrMixin(str):
  pass

class Color(StrMixin, Enum):
  RED = "red"
  GREEN = "green"
