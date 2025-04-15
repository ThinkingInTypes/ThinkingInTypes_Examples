# example_22.py
from generic_alias import Pair
from typing import get_origin, get_args
print(get_origin(Pair[int]))  # outputs: <class 'tuple'>
print(get_args(Pair[int]))    # outputs: (<class 'int'>, <class 'int'>)
