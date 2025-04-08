# example_8.py
from typing import TypeVar, Generic

T_contra = TypeVar("T_contra", contravariant=True)


class Processor(Generic[T_contra]):
    def process(self, value: T_contra) -> None:
        print(value)


int_processor: Processor[int] = Processor()
number_processor: Processor[float] = int_processor  # Valid due to contravariance
