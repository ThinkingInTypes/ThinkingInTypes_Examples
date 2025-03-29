# literal_types.py
from typing import Literal


def set_mode(mode: Literal["auto", "manual"]) -> None:
    print(f"Mode set to {mode}")


set_mode("auto")  # valid
## Mode set to auto
# set_mode('automatic')  # invalid, detected by type checker
