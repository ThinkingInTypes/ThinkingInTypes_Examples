# file_protocol.py
from typing import Protocol
from pathlib import Path
from io import StringIO


class Writable(Protocol):
    def write(self, __s: str) -> int: ...


def save_message(out: Writable, message: str) -> None:
    out.write(f"{message}\n")


# With a file:
file_path = Path("message.txt")
with file_path.open("w", encoding="utf-8") as f:
    save_message(f, "Hello, World!")

# With an in-memory buffer:
buffer = StringIO()
save_message(buffer, "Hello, Buffer!")
buffer.seek(0)
print(buffer.read())
## Hello, Buffer!
