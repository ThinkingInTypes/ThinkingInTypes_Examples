# unique_values.py
from enum import Enum, verify, UNIQUE

from book_utils import Catch

with Catch():

    @verify(UNIQUE)
    class Color(Enum):
        RED = 1
        GREEN = 2
        BLUE = 3
        DUPLICATE = 3
