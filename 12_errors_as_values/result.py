# result.py
# Generic Result with Success & Failure subtypes

from dataclasses import dataclass
from typing import Generic, TypeVar

ANSWER = TypeVar("ANSWER")
ERROR = TypeVar("ERROR")


class Result(Generic[ANSWER, ERROR]):
    pass


@dataclass(frozen=True)
class Success(Result[ANSWER, ERROR]):
    answer: ANSWER  # Usage: return Success(answer)

    def unwrap(self) -> ANSWER:
        return self.answer


@dataclass(frozen=True)
class Failure(Result[ANSWER, ERROR]):
    error: ERROR  # Usage: return Failure(error)
