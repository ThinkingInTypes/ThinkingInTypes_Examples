# basic_requires.py
from book_utils import Catch
from require import requires, Condition

positivity = Condition(
    check=lambda x: x > 0, message="x must be positive"
)


@requires(positivity)
def sqrt(x) -> float:
    return x ** 0.5


print(sqrt(4))
## 2.0
with Catch():
    sqrt(-2)
## Error: x must be positive
