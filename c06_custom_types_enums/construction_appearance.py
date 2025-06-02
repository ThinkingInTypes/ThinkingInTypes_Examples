from enum import Enum, IntEnum, StrEnum, auto


class N(Enum):
    ONE = 1
    TWO = 2
    THREE = 3


class N2(IntEnum):
    ONE = 1
    TWO = 2
    THREE = 3


class N3(IntEnum):  # Or Enum
    ONE = auto()
    TWO = auto()
    THREE = auto()


class S(Enum):
    A = "one"
    B = "two"
    C = "three"


class S2(StrEnum):
    A = "one"
    B = "two"
    C = "three"


# Enum members have name and value:
print(S.A.name)
print(S.A.value)

# Construction syntax returns corresponding value:
print(N(2))
print(S("one"))

# Look up by name string:
print(S["A"])
print(N["TWO"])

# All values:
print([member.value for member in S])

# Ordered by definition order, not value order:
print(list(S))

# Enum members are singletons:
print(S.C is S("three"))

# Internal maps:
print(N._member_map_)
print(N._value2member_map_)

# Query whether a value has a corresponding member:
print(2 in N._value2member_map_)
print("one" in S._value2member_map_)
