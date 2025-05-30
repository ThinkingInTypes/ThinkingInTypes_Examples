# example_4.py
from typing import runtime_checkable, Protocol
from file_resource import FileResource


@runtime_checkable
class Closable(Protocol):
    def close(self) -> None: ...


# FileResource has close():
print(isinstance(FileResource("data.txt"), Closable))
## True
