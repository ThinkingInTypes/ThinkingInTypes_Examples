# Bad examples from ChatGPT
from typing import Callable, Protocol


def call_twice(f: Callable[[int], int]) -> int:
    return f(42) + f(42)


def bad(x: int) -> int:
    print("got:", x)
    return "not an int"  # type: ignore  # Had to turn off type checking (Bad ChatGPT)


print(call_twice(bad))  # Type checker is happy


class StringProducer(Protocol):
    def produce(self) -> str: ...


class Lies:
    def produce(self) -> str:
        return 42  # ← Type checker trusts the annotation (Bad ChatGPT)


def print_uppercase(p: StringProducer) -> None:
    print(p.produce().upper())


liar = Lies()
print_uppercase(liar)
