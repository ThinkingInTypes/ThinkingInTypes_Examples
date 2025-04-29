# data_point.py
class DataPoint:
    measurement1 = None
    measurement2 = None
    measurement3 = None


d = DataPoint()
d.measurement1 = 100  # type: ignore
d.measurement2 = 200  # type: ignore
d.measurement3 = 300  # type: ignore
