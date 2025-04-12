# union_plus_optional.py
from typing import Optional


def f1(value: int | str | None) -> str:
    return str(value)


print(f1(42), f1("forty-two"), f1(None))
## 42 forty-two None


def f2(value: Optional[int | str]) -> str:
    return str(value)


print(f2(42), f2("forty-two"), f2(None))
## 42 forty-two None
