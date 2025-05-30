# dataclass_generated_methods.py
from point_dataclasses import (
    Point,
    OrderedPoint,
    FrozenPoint,
    OrderedFrozenPoint,
)
from class_methods import show_methods

show_methods(Point)
## class Point:
##   __annotate_func__(format, /)
##   __replace__(self, /, **changes)
##   __init__(self, x: int = 1, y: int = 2) -> None
##   __repr__(self)
##   __eq__(self, other)
show_methods(OrderedPoint)
## class OrderedPoint:
##   __annotate_func__(format, /)
##   __replace__(self, /, **changes)
##   __init__(self, x: int = 1, y: int = 2) -> None
##   __repr__(self)
##   __eq__(self, other)
##   __lt__(self, other)
##   __le__(self, other)
##   __gt__(self, other)
##   __ge__(self, other)
show_methods(FrozenPoint)
## class FrozenPoint:
##   __annotate_func__(format, /)
##   __replace__(self, /, **changes)
##   __hash__(self)
##   __init__(self, x: int = 1, y: int = 2) -> None
##   __repr__(self)
##   __eq__(self, other)
##   __setattr__(self, name, value)
##   __delattr__(self, name)
show_methods(OrderedFrozenPoint)
## class OrderedFrozenPoint:
##   __annotate_func__(format, /)
##   __replace__(self, /, **changes)
##   __hash__(self)
##   __init__(self, x: int = 1, y: int = 2) -> None
##   __repr__(self)
##   __eq__(self, other)
##   __lt__(self, other)
##   __le__(self, other)
##   __gt__(self, other)
##   __ge__(self, other)
##   __setattr__(self, name, value)
##   __delattr__(self, name)
