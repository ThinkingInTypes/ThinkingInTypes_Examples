# point_methods.py
from class_methods import show_methods


class Klass:
    def __init__(self, val: str):
        self.val = val


show_methods(Klass)
## class Klass:
##   __init__(self, val: str)
