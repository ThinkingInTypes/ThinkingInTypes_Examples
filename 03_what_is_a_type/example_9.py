# example_9.py
from pathlib import Path

from book_utils import Catch

this_dir = Path(__file__).parent.resolve()


def read_second_line(file: str | Path) -> str:
    # Converts string or Path to a Path object:
    p = this_dir / file
    return p.read_text().splitlines()[1]


# Works with a string path:
print(read_second_line("example_9.py"))
## from pathlib import Path
# Works with a Path object:
print(read_second_line(Path("example_9.py")))
## from pathlib import Path
with Catch():
    # Raises TypeError, static checker flags it:
    read_second_line(12345)  # type: ignore
## Error: unsupported operand type(s) for /: 'WindowsPath' and 'int'
