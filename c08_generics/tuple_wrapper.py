# tuple_wrapper.py


class TupleWrapper[*T]:
    def __init__(self, *values: *T):
        self.values = values


t1 = TupleWrapper(1)  # TupleWrapper[int]
t2 = TupleWrapper("a", 2, 3.14)  # TupleWrapper[str, int, float]
