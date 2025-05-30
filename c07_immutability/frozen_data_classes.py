# frozen_data_classes.py
from dataclasses import dataclass
from book_utils import Catch


@dataclass(frozen=True)
class Messenger:
    name: str
    number: int
    depth: float = 0.0  # Default


print(messenger := Messenger("foo", 12, 3.14))
## Messenger(name='foo', number=12, depth=3.14)
# Frozen dataclass is immutable:
with Catch():
    messenger.name = "bar"  # type: ignore

# Automatically creates __hash__():
d = {messenger: "value"}
print(d[messenger])
## value
