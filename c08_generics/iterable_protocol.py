# iterable_protocol.py
from typing import Iterator, Protocol


class IterableLike[T](Protocol):
    def __iter__(self) -> Iterator[T]: ...
