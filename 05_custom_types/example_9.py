# example_9.py
from dataclasses import dataclass, field
from book_utils import Catch


@dataclass(frozen=True)
class Order:
    order_id: int
    items: list[str] = field(default_factory=list)


order = Order(order_id=123)
with Catch():
    order.order_id = 456
## Error: cannot assign to field 'order_id'
