# demo_exception_checker.py
from dataclasses import dataclass
from book_utils import Catch


@dataclass
class Fob:
    x: int

    def __post_init__(self) -> None:
        if self.x < 0:
            raise ValueError(f"Fob arg {self.x} must be positive")


def foo(a: int, b: Fob) -> str:
    if a < 0:
        raise ValueError(f"foo arg {a} must be positive")
    return f"foo({a}, {b}) succeeded"


def mark(marker) -> None:
    print(f"[{marker}]:", end=" ")


# If you know it succeeds you can just run it without a context:
mark(1)
print(foo(0, Fob(0)))

mark(2)
with Catch():  # Single-failure simple form
    foo(1, Fob(-1))

# In the simple form, success does NOT automatically display the result:
mark(3)
with Catch():
    print(foo(42, Fob(42)))  # Must explicitly print
    # Or call print inside the function

mark(4)
with Catch() as catch:  # Lambda form displays successful result
    catch(lambda: foo(42, Fob(42)))

# Multi-failure block requires lambda form:
with Catch() as catch:
    mark("A")
    catch(lambda: foo(1, Fob(1)))
    mark("B")
    catch(lambda: foo(0, Fob(0)))
    mark("C")
    catch(lambda: foo(-1, Fob(1)))
    mark("D")
    catch(lambda: foo(1, Fob(-1)))
    mark("E")
    catch(lambda: foo(-1, Fob(-1)))
    mark("F")
    catch(lambda: foo(10, Fob(11)))

print("completed")
