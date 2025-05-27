# dataclass_attribute.py
from dataclasses import dataclass
from class_and_instance import show_dicts


@dataclass
class D:
    x: int = 1
    y: int = 2


d = D()
show_dicts(d, "d")
## D.__dict__ (class attributes):
##   x: 1
##   y: 2
## d.__dict__ (instance attributes):
##   x: 1
##   y: 2
## d.x is 1
## d.y is 2
d.x = 99
show_dicts(d, "d")
## D.__dict__ (class attributes):
##   x: 1  # overridden by instance
##   y: 2
## d.__dict__ (instance attributes):
##   x: 99
##   y: 2
## d.x is 99
## d.y is 2
d.y = 111
show_dicts(d, "d")
## D.__dict__ (class attributes):
##   x: 1  # overridden by instance
##   y: 2  # overridden by instance
## d.__dict__ (instance attributes):
##   x: 99
##   y: 111
## d.x is 99
## d.y is 111
