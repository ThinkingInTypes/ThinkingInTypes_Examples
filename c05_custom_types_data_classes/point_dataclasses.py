# point_dataclasses.py
from dataclasses import dataclass


@dataclass
class Point:
    x: int = 1
    y: int = 2


@dataclass(order=True)
class OrderedPoint:
    x: int = 1
    y: int = 2


@dataclass(frozen=True)
class FrozenPoint:
    x: int = 1
    y: int = 2


@dataclass(order=True, frozen=True)
class OrderedFrozenPoint:
    x: int = 1
    y: int = 2
