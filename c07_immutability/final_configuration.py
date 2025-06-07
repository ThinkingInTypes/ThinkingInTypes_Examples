# final_configuration.py
from pathlib import Path
from typing import Final


class Config:
    WIDTH: Final[int] = 65
    INPUT: Final[Path] = Path("infile.txt")
    OUTPUT: Final[Path] = Path("outfile.txt")
