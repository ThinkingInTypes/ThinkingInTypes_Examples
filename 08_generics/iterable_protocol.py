# iterable_protocol.py
from typing import Iterator, TypeVar, Protocol

T = TypeVar("T", covariant=True)


class IterableLike(Protocol[T]):
    def __iter__(self) -> Iterator[T]: ...
