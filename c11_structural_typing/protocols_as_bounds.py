# protocols_as_bounds.py
from logger_protocol import Logger


def f[T: Logger](x: T) -> T:
    x.log(f"In f({x})")
    return x


class C[T: Logger]:
    def f(self, x: T) -> T:
        x.log(f"In C.f({x})")
        return x
