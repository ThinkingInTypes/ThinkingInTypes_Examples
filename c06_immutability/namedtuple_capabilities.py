# namedtuple_capabilities.py
from collections import namedtuple
from typing import NamedTuple, Optional

# 1. Dynamically generating a NamedTuple:
Point1 = namedtuple("Point1", ["x", "y"])
p1 = Point1(10, 20)
print(f"{p1 = }, {type(p1) = }")
## p1 = Point1(x=10, y=20), type(p1) = <class
## '__main__.Point1'>


# 2. A simple immutable type:
class Point2(NamedTuple):
    x: int
    y: int


print(p2 := Point2(30, 40))
## Point2(x=30, y=40)


# 3. Default values:
class Employee(NamedTuple):
    name: str
    id: int = 0
    department: Optional[str] = None


print(f"Defaulted: {Employee('Alice')}")
## Defaulted: Employee(name='Alice', id=0,
## department=None)
print(f"Full: {Employee('Bob', 123, 'Engineering')}")
## Full: Employee(name='Bob', id=123,
## department='Engineering')


# 4. Methods:
class Circle(NamedTuple):
    radius: float | int

    def area(self) -> float:
        from math import pi

        return pi * (self.radius**2)


print(f"{(c := Circle(5))} {c.area():.2f}")
## Circle(radius=5) 78.54

# 5. NamedTuple utilities: _replace, _asdict, _fields:
print(f"Original Circle: {c}")
## Original Circle: Circle(radius=5)
c2 = c._replace(radius=10)
print(f"{c2 = }, {c = }")
## c2 = Circle(radius=10), c = Circle(radius=5)
print(f"Fields: {Circle._fields}")
## Fields: ('radius',)
print(f"As dict: {c2._asdict()}")
## As dict: {'radius': 10}

# 6. Sequence unpacking:
x_val, y_val = p2
print(f"{x_val = }, {y_val = }")
## x_val = 30, y_val = 40


# 7. Pattern matching
def describe_point(pt: Point2) -> str:
    match pt:
        case Point2(x, y) if x == y:
            return f"Diagonal point at ({x}, {y})"
        case Point2(x, y):
            return f"Point at x={x}, y={y}"
        case _:
            return "Unknown point"


print(describe_point(Point2(1, 1)))
## Diagonal point at (1, 1)
print(describe_point(Point2(2, 3)))
## Point at x=2, y=3


# 8. Nested NamedTuples:
class Address(NamedTuple):
    street: str
    city: str


class Person(NamedTuple):
    name: str
    age: int
    address: Address


addr = Address("123 Maple St", "Springfield")
person = Person("Carol", 29, addr)
print(
    f"{person.name = }, {person.age = }, {person.address.city = }"
)
## person.name = 'Carol', person.age = 29,
## person.address.city = 'Springfield'


# Nested pattern match:
def location_info(p: Person) -> str:
    match p:
        case Person(_, _, Address(_, city="Springfield")):
            return f"Resident of Springfield"
        case Person(name, _, Address(street, city)):
            return f"{name} lives at {street}, {city}"
        case _:
            return "Unknown location"


print(location_info(person))
## Resident of Springfield
