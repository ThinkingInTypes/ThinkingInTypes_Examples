# n_dimensional_tensor.py
from typing import (
    TypeVar,
    TypeVarTuple,
    Generic,
    Unpack,
    Literal,
    TypeAlias,
)

T = TypeVar("T")
Shape = TypeVarTuple("Shape")


class Tensor(Generic[T, Unpack[Shape]]):
    def __init__(
        self, data: list, *, shape: tuple[Unpack[Shape]]
    ):
        self.data = data
        self.shape = shape

    def __repr__(self) -> str:
        return f"Tensor(shape={self.shape})"


Shape3x3: TypeAlias = tuple[Literal[3], Literal[3]]
Shape2x2x2: TypeAlias = tuple[Literal[2], Literal[2], Literal[2]]

t1 = Tensor[float, *Shape3x3](data=[[1.0] * 3] * 3, shape=(3, 3))

t2 = Tensor[int, *Shape2x2x2](
    data=[[[1, 2], [3, 4]], [[5, 6], [7, 8]]],
    shape=(2, 2, 2),
)

print(t1)  # Tensor(shape=(3, 3))
## Tensor(shape=(3, 3))
print(t2)  # Tensor(shape=(2, 2, 2))
## Tensor(shape=(2, 2, 2))
