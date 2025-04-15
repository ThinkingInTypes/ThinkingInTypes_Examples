# example_21.py
from generic_alias import Pair
r: Pair = ("x", 5)  # type checker treats this as tuple[Any, Any]
