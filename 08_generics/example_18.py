# example_18.py
from typing import Protocol
from pathlib import Path
from io import StringIO

class Writable(Protocol):
    def write(self, data: str) -> None: ...

def save_message(out: Writable, message: str) -> None:
    out.write(f"{message}\n")

# Using an actual file:
file_path = Path("message.txt")
with file_path.open("w", encoding="utf-8") as f:
    save_message(f, "Hello, World!")

# Using an in-memory buffer:
buffer = StringIO()
save_message(buffer, "Hello, Buffer!")
buffer.seek(0)
print(buffer.read())  # prints "Hello, Buffer!\n"
