# proof_of_class_attribute.py
from class_and_instance import show_dicts


class A:
    x: int = 1
    y: int = 2


a = A()
show_dicts(a, "a")
## A.__dict__ (class attributes):
##   x: 1
##   y: 2
## a.__dict__ (instance attributes):
##   x: <not present>
##   y: <not present>
## a.x is 1
## a.y is 2
a.x = 99
show_dicts(a, "a")
## A.__dict__ (class attributes):
##   x: 1  # overridden by instance
##   y: 2
## a.__dict__ (instance attributes):
##   x: 99
##   y: <not present>
## a.x is 99
## a.y is 2
a.y = 111
show_dicts(a, "a")
## A.__dict__ (class attributes):
##   x: 1  # overridden by instance
##   y: 2  # overridden by instance
## a.__dict__ (instance attributes):
##   x: 99
##   y: 111
## a.x is 99
## a.y is 111
