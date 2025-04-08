# example_9.py
from typing import Protocol  
class SupportsClose(Protocol):  
    def close(self) -> None: ...
