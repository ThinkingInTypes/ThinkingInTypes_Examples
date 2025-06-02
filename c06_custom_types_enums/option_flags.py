from enum import Flag, auto


class Option(Flag):
    NONE = 0
    TRACE = auto()
    DEBUG = auto()
    VERBOSE = auto()
    SILENT = auto()
    SAVE = auto()


for k, v in Option.__members__.items():
    print(f"{k} = {v.value} ({v.value:08b})")

# Compose multiple options:
opt1 = Option.TRACE | Option.VERBOSE
print(f"{opt1 = } ({opt1.value:08b})")
opt2 = opt1 | Option.SAVE
print(f"{opt2 = } ({opt2.value:08b})")

# Usage
print(f"rw: {opt1}")
print(f"rwx: {opt2}")

# Check membership
if Option.TRACE in opt2:
    print("Trace option granted.")

if Option.VERBOSE not in opt2:
    print("Verbose option denied.")

# Invert options
all_options = (
    Option.TRACE
    | Option.DEBUG
    | Option.VERBOSE
    | Option.SILENT
    | Option.SAVE
)
# XOR: what options are missing from opt2:
missing = all_options ^ opt2
print(f"Missing options: {missing}")
