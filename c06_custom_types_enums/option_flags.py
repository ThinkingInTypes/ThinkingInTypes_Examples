# option_flags.py
from enum import Flag, auto


class Option(Flag):
    NONE = 0
    TRACE = auto()
    DEBUG = auto()
    VERBOSE = auto()
    SILENT = auto()
    SAVE = auto()

    @classmethod
    def all(cls) -> "Option":
        return (
            cls.TRACE
            | cls.DEBUG
            | cls.VERBOSE
            | cls.SILENT
            | cls.SAVE
        )


print([(member, member.name, member.value) for member in Option])
## [(<Option.TRACE: 1>, 'TRACE', 1), (<Option.DEBUG: 2>, 'DEBUG',
## 2), (<Option.VERBOSE: 4>, 'VERBOSE', 4), (<Option.SILENT: 8>,
## 'SILENT', 8), (<Option.SAVE: 16>, 'SAVE', 16)]

for k, v in Option.__members__.items():
    print(f"{k} = {v.value} ({v.value:08b})")
## NONE = 0 (00000000)
## TRACE = 1 (00000001)
## DEBUG = 2 (00000010)
## VERBOSE = 4 (00000100)
## SILENT = 8 (00001000)
## SAVE = 16 (00010000)

# Compose options:
opt1 = Option.TRACE | Option.VERBOSE
# Combined flags produce symbolic names, not just numbers:
print(f"{opt1 = } ({opt1.value:08b})")
## opt1 = <Option.TRACE|VERBOSE: 5> (00000101)
opt2 = opt1 | Option.SAVE
print(f"{opt2 = } ({opt2.value:08b})")
## opt2 = <Option.TRACE|VERBOSE|SAVE: 21> (00010101)

# Membership:
print(f"{Option.TRACE in opt2 = }")
## Option.TRACE in opt2 = True
print(f"{Option.VERBOSE not in opt2 = }")
## Option.VERBOSE not in opt2 = False

# Bitwise AND: what options are present in both:
print(f"{opt2 & Option.VERBOSE = }")
## opt2 & Option.VERBOSE = <Option.VERBOSE: 4>
print(f"{opt2 & Option.DEBUG = }")
## opt2 & Option.DEBUG = <Option.NONE: 0>

# Equivalence:
print(f"{(opt2 & Option.SAVE) != Option.NONE = }")
## (opt2 & Option.SAVE) != Option.NONE = True

# Bitwise XOR: what options are missing from opt2:
print(f"Missing: {Option.all() ^ opt2}")
## Missing: Option.DEBUG|SILENT
