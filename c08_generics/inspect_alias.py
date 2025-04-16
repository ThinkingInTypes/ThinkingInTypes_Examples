# inspect_alias.py
from generic_alias import Pair
from typing import get_origin, get_args

print(get_origin(Pair[int]))
## <class 'tuple'>
print(get_args(Pair[int]))
## (<class 'int'>, <class 'int'>)
