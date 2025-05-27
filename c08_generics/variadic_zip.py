# variadic_zip.py


def zip_variadic[*T](
    *args: tuple[*T],
) -> tuple[tuple[*T], ...]:
    return tuple(zip(*args))


def unzip_variadic[*T](
    packed: tuple[tuple[*T], ...],
) -> tuple[tuple[*T], ...]:
    return tuple(zip(*packed))


a: tuple[int, str, float] = (1, "a", 3.14)
b: tuple[int, str, float] = (2, "b", 2.71)
c: tuple[int, str, float] = (3, "c", 1.41)

zipped = zip_variadic(a, b, c)
unzipped = unzip_variadic(zipped)

print(f"Zipped: {zipped}")
## Zipped: ((1, 2, 3), ('a', 'b', 'c'), (3.14,
## 2.71, 1.41))
# Zipped: ((1, 2, 3), ('a', 'b', 'c'), (3.14, 2.71, 1.41))
print(f"Unzipped: {unzipped}")
## Unzipped: ((1, 'a', 3.14), (2, 'b', 2.71), (3,
## 'c', 1.41))
# Unzipped: ((1, 'a', 3.14), (2, 'b', 2.71), (3, 'c', 1.41))
