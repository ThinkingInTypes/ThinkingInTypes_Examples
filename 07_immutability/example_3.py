# example_3.py
from typing import Final

RATE: Final = 3000


class BaseConfig:
    TIMEOUT: Final[int] = 60


class SubConfig(BaseConfig):
    # Error: can't override a final attribute in BaseConfig
    TIMEOUT = 30  # type: ignore
