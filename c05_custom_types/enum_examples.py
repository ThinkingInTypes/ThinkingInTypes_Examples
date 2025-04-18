# enum_examples.py
"""
Comprehensive demonstration of Enum capabilities.
"""
from enum import Enum, auto, unique, IntEnum, StrEnum, Flag, IntFlag


# 1. Basic Enum definition
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


print(Color.RED)
print(Color.RED.name, Color.RED.value)


# 2. Enum with auto values
class Status(Enum):
    PENDING = auto()
    RUNNING = auto()
    DONE = auto()


print(list(Status))


# 3. Custom values and types
class HttpStatus(IntEnum):
    OK = 200
    NOT_FOUND = 404
    INTERNAL_ERROR = 500


print(f"HttpStatus.OK = {HttpStatus.OK}, as int: {int(HttpStatus.OK)}")

# 4. Iteration and comparison
for color in Color:
    print(f"Color: {color.name} = {color.value}")

print(Color.RED == Color.RED)
print(Color.RED is Color.RED)
print(Color.RED == Color.GREEN)

# 5. Access by name and value
print(Color["BLUE"])
print(Color(2))  # GREEN


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
print(f"JSON-ready: {Fruit.BANANA!r}")


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


# 9. Aliases
class Mood(Enum):
    HAPPY = 1
    JOYFUL = 1  # Alias
    SAD = 2


print(f"Members: {[m for m in Mood]}")  # Only one member per value
print(f"Alias: {Mood.JOYFUL is Mood.HAPPY}")


# 10. Bitwise Flags
class Permission(Flag):
    READ = auto()
    WRITE = auto()
    EXECUTE = auto()


user_perm = Permission.READ | Permission.WRITE  # type: ignore
print(f"User permissions: {user_perm}")
print(f"Can execute? {Permission.EXECUTE in user_perm}")


# IntFlag for bitwise checks with ints
class Access(IntFlag):
    NONE = 0
    READ = 1
    WRITE = 2
    EXECUTE = 4


perm = Access.READ | Access.EXECUTE
print(f"perm & Access.WRITE: {perm & Access.WRITE}")
print(f"perm has EXECUTE: {bool(perm & Access.EXECUTE)}")

# 11. Pattern matching
status = Status.DONE
match status:
    case Status.PENDING:
        print("Job is pending")
    case Status.RUNNING:
        print("Job is in progress")
    case Status.DONE:
        print("Job completed")
