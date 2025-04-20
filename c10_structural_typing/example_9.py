# example_9.py
from typing import TypeVar
from logger_protocol import Logger

T = TypeVar("T", bound=Logger)
