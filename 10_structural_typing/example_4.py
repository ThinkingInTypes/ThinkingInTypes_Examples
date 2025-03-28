# example_4.py
from typing import runtime_checkable, Protocol


@runtime_checkable
class Closable(Protocol):
    def close(self) -> None: ...


isinstance(FileResource("data.txt"), Closable)  # True, because FileResource has close()
