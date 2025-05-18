# tuple_wrapper.py

class TupleWrapper[*Ts]:
    def __init__(self, *values: *Ts):
        self.values = values


t1 = TupleWrapper(1)  # TupleWrapper[int]
t2 = TupleWrapper("a", 2, 3.14)  # TupleWrapper[str, int, float]
