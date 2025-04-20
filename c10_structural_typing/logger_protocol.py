# logger_protocol.py
from contextlib import AbstractContextManager
from pathlib import Path
from typing import Protocol


class Logger(Protocol):
    def log(self, message: str) -> None: ...


class FileLogger(AbstractContextManager):
    """
    Logger that writes to a known log file in a fixed directory.
    """

    def __init__(self, path: Path = Path("./log.txt")):
        path.parent.mkdir(parents=True, exist_ok=True)
        self.filename = path
        self._file = self.filename.open("w", encoding="utf-8")

    def log(self, message: str) -> None:
        self._file.write(message + "\n")
        self._file.flush()

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        self._file.close()


class ListLogger:
    """
    Logger that stores messages in a list
    """

    def __init__(self):
        self.messages: list[str] = []

    def log(self, message: str) -> None:
        self.messages.append(message)


def run_process(task_name: str, logger: Logger) -> None:
    logger.log(f"Starting {task_name}")
    # Perform the task ...
    logger.log(f"Finished {task_name}")
