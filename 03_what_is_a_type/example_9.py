# example_9.py
from pathlib import Path

from book_utils import Catch


def read_first_line(path: str | Path) -> str:
    p = Path(
        path
    )  # convert string or Path to a Path object
    return p.read_text().splitlines()[0]


# Works with a string path:
print(read_first_line("example_9.py"))
# Works with a Path object:
print(read_first_line(Path("example_9.py")))
with Catch():
    # Raises TypeError, static checker flags it:
    print(read_first_line(12345))  # type: ignore
