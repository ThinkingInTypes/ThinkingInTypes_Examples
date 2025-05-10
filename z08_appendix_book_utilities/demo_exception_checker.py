# demo_exception_checker.py
from dataclasses import dataclass

from book_utils import Catch


@dataclass
class Fob:
    x: int

    def __post_init__(self) -> None:
        if self.x < 0:
            raise ValueError(
                f"Fob arg {self.x} must be positive"
            )


def foo(a: int, b: Fob) -> str:
    if a < 0:
        raise ValueError(f"foo arg {a} must be positive")
    return f"foo({a}, {b}) succeeded"


# If you know it succeeds you can just run it without a context:
print(foo(0, Fob(0)))
## foo(0, Fob(x=0)) succeeded
with Catch():  # Single-failure form
    foo(1, Fob(-1))
## Error: Fob arg -1 must be positive

# In the form, success does NOT automatically display the result:
with Catch():
    print(foo(42, Fob(42)))  # Must explicitly print
## foo(42, Fob(x=42)) succeeded

# Lambda form displays successful result:
with Catch() as catch:
    catch(lambda: foo(42, Fob(42)))
## foo(42, Fob(x=42)) succeeded

# Multi-failure block requires lambda form:
with Catch() as catch:
    catch(lambda: foo(1, Fob(1)))
    catch(lambda: foo(0, Fob(0)))
    catch(lambda: foo(-1, Fob(1)))
    catch(lambda: foo(1, Fob(-1)))
    catch(lambda: foo(-1, Fob(-1)))
    catch(lambda: foo(10, Fob(11)))
## foo(1, Fob(x=1)) succeeded
## foo(0, Fob(x=0)) succeeded
## Error: foo arg -1 must be positive
## Error: Fob arg -1 must be positive
## Error: Fob arg -1 must be positive
## foo(10, Fob(x=11)) succeeded
