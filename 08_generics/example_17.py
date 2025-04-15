# example_17.py
from typing import Iterator, TypeVar, Protocol

T = TypeVar('T')
class IterableLike(Protocol[T]):
    def __iter__(self) -> Iterator[T]:
        ...
