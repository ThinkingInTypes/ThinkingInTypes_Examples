# custom_and_generated.py
from enum import Enum, auto


class N(Enum):
    ONE = 1
    TWO = 2
    THREE = 3


# Auto-Generate Sequential Values
class N2(Enum):
    ONE = auto()
    TWO = auto()
    THREE = auto()


# Enum values can be types other than int:
class Color(Enum):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"


# Access all members
print(f"{N.__members__ = }")
## N.__members__ = mappingproxy({'ONE': <N.ONE: 1>, 'TWO': <N.TWO:
## 2>, 'THREE': <N.THREE: 3>})
print(f"{N2.__members__ = }")
## N2.__members__ = mappingproxy({'ONE': <N2.ONE: 1>, 'TWO':
## <N2.TWO: 2>, 'THREE': <N2.THREE: 3>})
print(f"{Color.__members__ = }")
## Color.__members__ = mappingproxy({'RED': <Color.RED: 'red'>,
## 'GREEN': <Color.GREEN: 'green'>, 'BLUE': <Color.BLUE: 'blue'>})
# All names:
print([member.name for member in Color])
## ['RED', 'GREEN', 'BLUE']
# All values:
print([member.value for member in Color])
## ['red', 'green', 'blue']
# Ordered by definition order, not value order:
print(list(Color))
## [<Color.RED: 'red'>, <Color.GREEN: 'green'>, <Color.BLUE:
## 'blue'>]
# Enum members are singletons:
print(Color.RED is Color("red"))
## True
# Internal maps:
print(N._member_map_)
## {'ONE': <N.ONE: 1>, 'TWO': <N.TWO: 2>, 'THREE': <N.THREE: 3>}
print(N._value2member_map_)
## {1: <N.ONE: 1>, 2: <N.TWO: 2>, 3: <N.THREE: 3>}
# Check if a value has a corresponding member:
print(2 in N._value2member_map_)
## True
print("blue" in Color._value2member_map_)
## True
