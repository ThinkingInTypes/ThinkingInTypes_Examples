# example_3.py
from typing import Final

RATE: Final = 3000


class BaseConfig:
    TIMEOUT: Final[int] = 60


# Error: can't override a final attribute in BaseConfig
class SubConfig(BaseConfig):
    TIMEOUT = 30  # type: ignore
