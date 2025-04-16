# file_resource.py
from typing import Protocol, Iterable


class Closable(Protocol):
    def close(self) -> None: ...


class FileResource:
    def __init__(self, path: str):
        self.file = open(path, "w")

    def close(self) -> None:
        self.file.close()


class SocketResource:
    def close(self) -> None:
        print("Socket closed")


def close_all(resources: Iterable[Closable]) -> None:
    for res in resources:
        res.close()


# All these have a close():
closables = (
    FileResource("data.txt"),
    SocketResource(),
    open("other.txt", "w"),
)
close_all(closables)
## Socket closed
