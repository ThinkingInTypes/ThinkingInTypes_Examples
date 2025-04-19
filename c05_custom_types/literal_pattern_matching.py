# literal_pattern_matching.py
from typing import Literal

Command = Literal["start", "stop", "pause"]


def run_command(cmd: Command) -> str:
    match cmd:
        case "start":
            return "System starting..."
        case "stop":
            return "System stopping..."
        case "pause":
            return "System pausing..."
        # Should not need this; some type checkers
        # require it anyway:
        case _:  # Unreachable
            raise ValueError(f"Unhandled command: {cmd}")


def run_string(cmd: str) -> str | None:
    match cmd:
        case "start":
            return "System starting..."
        case "stop":
            return "System stopping..."
        case "pause":
            return "System pausing..."
    return None
