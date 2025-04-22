# file_resource.py
from typing import Protocol


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
