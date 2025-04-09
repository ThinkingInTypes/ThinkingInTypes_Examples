# example_8.py
from dataclasses import dataclass, field


@dataclass(frozen=True)
class Rectangle:
    width: float
    height: float
    area: float = field(
        init=False
    )  # area will be computed, not passed by caller

    def __post_init__(self):
        # Bypass immutability to set the derived field
        object.__setattr__(
            self, "area", self.width * self.height
        )
