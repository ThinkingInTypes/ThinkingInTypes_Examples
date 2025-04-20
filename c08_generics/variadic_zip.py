# variadic_zip.py
from typing import TypeVarTuple, Unpack, Tuple, Any

Ts = TypeVarTuple("Ts")


def zip_variadic(
    *args: tuple[Unpack[Ts]],
) -> tuple[Tuple[*Ts], ...]:
    return tuple(zip(*args))


def unzip_variadic(
    packed: tuple[tuple[Any, ...], ...],
) -> tuple[tuple[Any, ...], ...]:
    return tuple(zip(*packed))


a: tuple[int, str, float] = (1, "a", 3.14)
b: tuple[int, str, float] = (2, "b", 2.71)
c: tuple[int, str, float] = (3, "c", 1.41)

zipped = zip_variadic(a, b, c)
unzipped = unzip_variadic(zipped)

print("Zipped:", zipped)
## Zipped: ((1, 2, 3), ('a', 'b', 'c'), (3.14,
## 2.71, 1.41))
print("Unzipped:", unzipped)
## Unzipped: ((1, 'a', 3.14), (2, 'b', 2.71), (3,
## 'c', 1.41))
