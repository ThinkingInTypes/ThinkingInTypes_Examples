# n_dimensional_tensor.py
from typing import TypeVar, TypeVarTuple, Generic, Unpack

# Data type (e.g., float, int):
T = TypeVar("T")
# A tuple of ints representing dimensions:
Shape = TypeVarTuple("Shape")


class Tensor(Generic[T, Unpack[Shape]]):

    def __init__(self, data: list, *, shape: tuple[Unpack[Shape]]):
        self.data = data
        self.shape = shape


def __repr__(self) -> str:
    return f"Tensor(shape={self.shape})"


t1 = Tensor[float, 3, 3](data=[[1.0] * 3] * 3, shape=(3, 3))  # 2D
t2 = Tensor[int, 2, 2, 2](data=[[[1, 2], [3, 4]], [[5, 6], [7, 8]]], shape=(2, 2, 2))  # 3D

print(t1)  # Tensor(shape=(3, 3))
print(t2)  # Tensor(shape=(2, 2, 2))
