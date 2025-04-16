# tuple_wrapper.py
from typing import Generic, TypeVarTuple

Ts = TypeVarTuple("Ts")


class TupleWrapper(Generic[*Ts]):
    def __init__(self, *values: *Ts):
        self.values = values


t1 = TupleWrapper(1)  # TupleWrapper[int]
t2 = TupleWrapper("a", 2, 3.14)  # TupleWrapper[str, int, float]
