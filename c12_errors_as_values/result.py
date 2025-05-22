# result.py
# Generic Result with Success & Failure subtypes
from dataclasses import dataclass


class Result[ANSWER, ERROR]:
    pass


@dataclass(frozen=True)
class Success[ANSWER, ERROR](Result[ANSWER, ERROR]):
    answer: ANSWER  # Usage: return Success(answer)

    def unwrap(self) -> ANSWER:
        return self.answer


@dataclass(frozen=True)
class Failure[ANSWER, ERROR](Result[ANSWER, ERROR]):
    error: ERROR  # Usage: return Failure(error)
