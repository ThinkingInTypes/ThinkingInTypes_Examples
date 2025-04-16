# generic_alias_tuple.py
from generic_alias import Pair

# type checker treats this as tuple[Any, Any]:
r: Pair = ("x", 5,)
