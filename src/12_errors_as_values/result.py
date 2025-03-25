# result.py
# Generic Result with Success & Failure subtypes
from dataclasses import dataclass
from typing import Generic, TypeVar, NamedTuple

ANSWER = TypeVar("ANSWER")  # Generic parameters
ERROR = TypeVar("ERROR")


class Result(Generic[ANSWER, ERROR]):
    pass


class Success(NamedTuple, Result[ANSWER, ERROR]):
    answer: ANSWER  # Usage: return Success(answer)

    def unwrap(self) -> ANSWER:
        return self.answer


class Failure(NamedTuple, Result[ANSWER, ERROR]):
    error: ERROR  # Usage: return Failure(error)
