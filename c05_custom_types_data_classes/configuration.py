# configuration.py
from pathlib import Path


class Config:
    WIDTH = 65
    INPUT = Path("infile.txt")
    OUTPUT = Path("outfile.txt")


print(Config.WIDTH)
## 65
print(Config.INPUT)
## infile.txt
print(Config.OUTPUT)
## outfile.txt
