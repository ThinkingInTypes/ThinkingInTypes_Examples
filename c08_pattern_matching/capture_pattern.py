# capture_pattern.py
from typing import Any


def quit_or_other(command: Any) -> None:
    match command:
        case "quit":
            print("Quitting...")
        case other:
            print(f"Received unknown command: {other!r}")


quit_or_other("quit")
## Quitting...
quit_or_other("hello")
## Received unknown command: 'hello'
