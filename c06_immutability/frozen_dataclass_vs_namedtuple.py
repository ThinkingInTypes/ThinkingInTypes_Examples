# frozen_dataclass_vs_namedtuple.py
from dataclasses import dataclass, field
from typing import NamedTuple, Any


# 1. Per-instance mutable default values via default_factory
@dataclass(frozen=True)
class Config:
    options: list[str] = field(default_factory=list)


c1 = Config()
c2 = Config()
c1.options.append("x")
print(f"c1.options={c1.options}")  # ['x']
## c1.options=['x']
print(f"c2.options={c2.options}")  # []
## c2.options=[]

# NamedTuple cannot use default_factory; defaults share same object
# This is forced to use a single default list if provided, and no factory.
PointNT = NamedTuple("PointNT", [("tags", list[str])])


# 2. Validation and invariants via __post_init__
@dataclass(frozen=True)
class Person:
    name: str
    age: int

    def __post_init__(self) -> None:
        if self.age < 0:
            raise ValueError(
                f"Age must be non-negative: {self.age}"
            )


try:
    Person("Eve", -5)
except ValueError as e:
    print(f"Validation: {e}")
## Validation: Age must be non-negative: -5


# 3. Computed/derived fields with init=False
@dataclass(frozen=True)
class Rectangle:
    width: float
    height: float
    area: float = field(init=False)

    def __post_init__(self) -> None:
        object.__setattr__(
            self, "area", self.width * self.height
        )


rect = Rectangle(3.0, 4.0)
print(f"Rectangle area={rect.area}")  # 12.0
## Rectangle area=12.0


# 4. Hiding sensitive fields via repr
@dataclass(frozen=True)
class Credentials:
    username: str
    password: str = field(repr=False)


cred = Credentials("user1", "s3cr3t")
print(f"Credentials repr: {cred}")
## Credentials repr: Credentials(username='user1')


# 5. Keyword-only fields enforcement:
@dataclass(frozen=True)
class Point:
    x: int
    y: int
    z: int = field(init=False)

    def __post_init__(self) -> None:
        object.__setattr__(self, "z", self.x + self.y)


# Positional-only: x, y; z computed
p = Point(1, 2)
print(f"Point(z computed): {p}")
## Point(z computed): Point(x=1, y=2, z=3)


# 6. Automatic ordering methods
@dataclass(order=True, frozen=True)
class Version:
    major: int
    minor: int
    patch: int


v1 = Version(1, 0, 0)
v2 = Version(1, 1, 0)
print(f"v1 < v2: {v1 < v2}")
## v1 < v2: True


# 7. Customizing equality/hash behavior
@dataclass(frozen=True, eq=False, unsafe_hash=True)
class IDWrapper:
    id_value: Any

    def __eq__(self, other: object) -> bool:
        if isinstance(other, IDWrapper):
            return self.id_value == other.id_value
        return NotImplemented


w1 = IDWrapper(10)
w2 = IDWrapper(10)
print(
    f"Custom eq w1 == w2: {w1 == w2}, hash(w1)==hash(w2): {hash(w1) == hash(w2)}"
)
## Custom eq w1 == w2: True, hash(w1)==hash(w2):
## True


# 8. Using slots for memory optimization:
@dataclass(frozen=True, slots=True)
class Point3D:
    x: int
    y: int
    z: int


pt = Point3D(0, 0, 0)
print(f"Point3D slots: {pt}")  # No __dict__, uses slots
## Point3D slots: Point3D(x=0, y=0, z=0)
