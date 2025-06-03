# unique_values.py
# pyright: reportArgumentType=false
from enum import Enum, unique

from book_utils import Catch

with Catch():

    @unique
    class Color(Enum):
        RED = 1
        GREEN = 2
        BLUE = 3
        DUPLICATE = 3
## Error: duplicate values found in <enum 'Color'>: DUPLICATE ->
## BLUE
