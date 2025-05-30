# dataclass_with_init.py
from dataclasses import dataclass
from class_and_instance import show_dicts
from class_methods import show_methods


@dataclass
class DI:
    x: int = 1
    y: int = 2

    def __init__(self):
        pass


show_methods(DI)
## class DI:
##   __init__(self)
##   __annotate_func__(format, /)
##   __replace__(self, /, **changes)
##   __repr__(self)
##   __eq__(self, other)
di = DI()
show_dicts(di, "di")
## DI.__dict__ (class attributes):
##   x: 1
##   y: 2
## di.__dict__ (instance attributes):
##   x: <not present>
##   y: <not present>
## di.x is 1
## di.y is 2
di.x = 99
show_dicts(di, "di")
## DI.__dict__ (class attributes):
##   x: 1  # Hidden by instance attribute
##   y: 2
## di.__dict__ (instance attributes):
##   x: 99
##   y: <not present>
## di.x is 99
## di.y is 2
di.y = 111
show_dicts(di, "di")
## DI.__dict__ (class attributes):
##   x: 1  # Hidden by instance attribute
##   y: 2  # Hidden by instance attribute
## di.__dict__ (instance attributes):
##   x: 99
##   y: 111
## di.x is 99
## di.y is 111
