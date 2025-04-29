# enum_examples.py
"""
Comprehensive demonstration of Enum capabilities.
"""

from enum import (
    Enum,
    auto,
    unique,
    IntEnum,
    StrEnum,
    Flag,
    IntFlag,
)


# 1. Basic Enum definition
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


print(Color.RED)
## Color.RED
print(Color.RED.name, Color.RED.value)
## RED 1


# 2. Enum with auto values
class Status(Enum):
    PENDING = auto()
    RUNNING = auto()
    DONE = auto()


print(list(Status))
## [<Status.PENDING: 1>, <Status.RUNNING: 2>,
## <Status.DONE: 3>]


# 3. Custom values and types
class HttpStatus(IntEnum):
    OK = 200
    NOT_FOUND = 404
    INTERNAL_ERROR = 500


print(f"HttpStatus.OK = {HttpStatus.OK}, as int: {int(HttpStatus.OK)}")
## HttpStatus.OK = 200, as int: 200

# 4. Iteration and comparison
for color in Color:
    print(f"Color: {color.name} = {color.value}")
## Color: RED = 1
## Color: GREEN = 2
## Color: BLUE = 3

print(Color.RED == Color.RED)
## True
print(Color.RED is Color.RED)
## True
print(Color.RED == Color.GREEN)
## False

# 5. Access by name and value
print(Color["BLUE"])
## Color.BLUE
print(Color(2))  # GREEN
## Color.GREEN


# 6. Unique constraint
@unique
class Direction(Enum):
    NORTH = 1
    SOUTH = 2
    EAST = 3
    WEST = 4
    # UP = 1  # Uncommenting this would raise ValueError for duplicate


# 7. Subclassing str or int for JSON-friendliness
class Fruit(StrEnum):
    APPLE = "apple"
    BANANA = "banana"


print(Fruit.APPLE.upper())
## APPLE
print(f"JSON-ready: {Fruit.BANANA!r}")
## JSON-ready: <Fruit.BANANA: 'banana'>


# 8. Methods and properties on Enums
class Shape(Enum):
    CIRCLE = auto()
    SQUARE = auto()

    def sides(self) -> int:
        return {
            Shape.CIRCLE: 0,
            Shape.SQUARE: 4,
        }[self]


print(f"Shape.CIRCLE has {Shape.CIRCLE.sides()} sides")
## Shape.CIRCLE has 0 sides


# 9. Aliases
class Mood(Enum):
    HAPPY = 1
    JOYFUL = 1  # Alias
    SAD = 2


print(f"Members: {[m for m in Mood]}")  # Only one member per value
## Members: [<Mood.HAPPY: 1>, <Mood.SAD: 2>]
print(f"Alias: {Mood.JOYFUL is Mood.HAPPY}")
## Alias: True


# 10. Bitwise Flags
class Permission(Flag):
    READ = auto()
    WRITE = auto()
    EXECUTE = auto()


user_perm = Permission.READ | Permission.WRITE  # type: ignore
print(f"User permissions: {user_perm}")
## User permissions: Permission.READ|WRITE
print(f"Can execute? {Permission.EXECUTE in user_perm}")
## Can execute? False


# IntFlag for bitwise checks with ints
class Access(IntFlag):
    NONE = 0
    READ = 1
    WRITE = 2
    EXECUTE = 4


perm = Access.READ | Access.EXECUTE
print(f"perm & Access.WRITE: {perm & Access.WRITE}")
## perm & Access.WRITE: 0
print(f"perm has EXECUTE: {bool(perm & Access.EXECUTE)}")
## perm has EXECUTE: True

# 11. Pattern matching
status = Status.DONE
match status:
    case Status.PENDING:
        print("Job is pending")
    case Status.RUNNING:
        print("Job is in progress")
    case Status.DONE:
        print("Job completed")
## Job completed
