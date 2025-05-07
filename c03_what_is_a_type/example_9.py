# example_9.py
from pathlib import Path

from book_utils import Catch


def is_file(file: str | Path) -> bool:
    # Converts string or Path to a Path object:
    p = Path(file)
    return p.exists() and p.is_file()


# Works with a string path:
print(is_file("nonexistent.txt"))
## False
# Works with a Path object:
print(is_file(Path("nonexistent.txt")))
## False
with Catch():
    # Raises TypeError, static checker flags it:
    is_file(12345)  # type: ignore
