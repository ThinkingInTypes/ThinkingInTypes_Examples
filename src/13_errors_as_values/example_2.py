# example_2.py
from dataclasses import dataclass
from typing import Generic, TypeVar

A = TypeVar('A')  # Successful result type
E = TypeVar('E')  # Error type

@dataclass(frozen=True)
class Result(Generic[A, E]):
    pass

@dataclass(frozen=True)
class Success(Result[A, E]):
    answer: A

    def unwrap(self) -> A:
        return self.answer

@dataclass(frozen=True)
class Failure(Result[A, E]):
    error: E
