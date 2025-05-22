# result_with_bind.py
from __future__ import annotations

from dataclasses import dataclass
from typing import Callable


class Result[ANSWER, ERROR]:
    def bind(
            self, func: Callable[[ANSWER], Result]
    ) -> Result[ANSWER, ERROR]:
        if isinstance(self, Success):
            return func(self.unwrap())
        return self  # Pass the Failure forward


@dataclass(frozen=True)
class Success[ANSWER, ERROR]:
    answer: ANSWER

    def unwrap(self) -> ANSWER:
        return self.answer


@dataclass(frozen=True)
class Failure[ANSWER, ERROR]:
    error: ERROR
