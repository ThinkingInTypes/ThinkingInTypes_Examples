# intflag_vs_flag.py
from enum import Flag, IntFlag, auto

from book_utils import Catch


class Flags(Flag):
    FIRST = auto()
    SECOND = auto()
    THIRD = auto()


class IntFlags(IntFlag):
    FIRST = auto()
    SECOND = auto()
    THIRD = auto()


# Both auto-assign powers of two:
for k, v in Flags.__members__.items():
    print(f"{k} = {v.value} ({v.value:08b})")
## FIRST = 1 (00000001)
## SECOND = 2 (00000010)
## THIRD = 4 (00000100)

defined = 3  # FIRST | SECOND
undefined = 903

# Both lookups succeed:
print(f"{IntFlags(defined) = }")
## IntFlags(defined) = <IntFlags.FIRST|SECOND: 3>
print(f"{Flags(defined) = }")
## Flags(defined) = <Flags.FIRST|SECOND: 3>

# IntFlags accepts any value:
print(f"{IntFlags(undefined) = }")
## IntFlags(undefined) = <IntFlags.FIRST|SECOND|THIRD|896: 903>

# Flags requires defined value:
with Catch():
    Flags(undefined)
## Error: <flag 'Flags'> invalid value 903
##     given 0b0 1110000111
##   allowed 0b0 0000000111
