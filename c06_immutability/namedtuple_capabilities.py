# namedtuple_capabilities.py
from collections import namedtuple
from typing import NamedTuple, Optional

# 1. Dynamically generating a NamedTuple:
Point1 = namedtuple("Point1", ["x", "y"])
p1 = Point1(10, 20)
print(f"{p1 = }, {type(p1) = }")


# 2. A simple immutable type:
class Point2(NamedTuple):
    x: int
    y: int


print(p2 := Point2(30, 40))


# 3. Default values:
class Employee(NamedTuple):
    name: str
    id: int = 0
    department: Optional[str] = None


print(f"Defaulted: {Employee("Alice")}")
print(f"Full: {Employee("Bob", 123, "Engineering")}")


# 4. Methods:
class Circle(NamedTuple):
    radius: float | int

    def area(self) -> float:
        from math import pi
        return pi * (self.radius ** 2)


print(f"{(c := Circle(5))} {c.area():.2f}")

# 5. NamedTuple utilities: _replace, _asdict, _fields:
print(f"Original Circle: {c}")
c2 = c._replace(radius=10)
print(f"{c2 = }, {c = }")
print(f"Fields: {Circle._fields}")
print(f"As dict: {c2._asdict()}")

# 6. Sequence unpacking:
x_val, y_val = p2
print(f"{x_val = }, {y_val = }")


# 7. Pattern matching
def describe_point(pt: Point2) -> str:
    match pt:
        case Point2(x, y) if x == y:
            return f"Diagonal point at ({x}, {y})"
        case Point2(x, y):
            return f"Point at x={x}, y={y}"


print(describe_point(Point2(1, 1)))
print(describe_point(Point2(2, 3)))


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
print(f"{person.name = }, {person.age = }, {person.address.city = }")


# Nested pattern match: 
def location_info(p: Person) -> str:
    match p:
        case Person(_, _, Address(_, city="Springfield")):
            return f"Resident of Springfield"
        case Person(name, _, Address(street, city)):
            return f"{name} lives at {street}, {city}"


print(location_info(person))
