# example_9.py
from pathlib import Path

from book_utils import Catch

this_dir = Path(__file__).parent.resolve()


def read_first_line(file: str | Path) -> str:
    print(f"read_first_line({file})")
    # Converts string or Path to a Path object:
    p = this_dir / file
    print(f"read_first_line: {p = }")
    first = p.read_text().splitlines()[0]
    print(f"read_first_line({file}) -> {first}")
    return p.read_text().splitlines()[0]


# Works with a string path:
print(read_first_line("./example_9.py"))
# Works with a Path object:
print(read_first_line(Path("./example_9.py")))
with Catch():
    # Raises TypeError, static checker flags it:
    read_first_line(12345)  # type: ignore
