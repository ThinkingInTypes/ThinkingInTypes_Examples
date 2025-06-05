# continuous_values.py
# pyright: reportArgumentType=false
from enum import Enum, verify, CONTINUOUS

from book_utils import Catch

with Catch():

    @verify(CONTINUOUS)
    class Status(Enum):
        OK = 1
        WARNING = 2
        ERROR = 3
        MISSING = 5  # error: gap
## Error: invalid enum 'Status': missing values 4
