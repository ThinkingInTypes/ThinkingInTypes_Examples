# return_result_demo.py
from pprint import pprint
from return_result import func_a

pprint([(i, func_a(i)) for i in range(5)])
## [(0, <Success: 0>),
##  (1, <Failure: func_a(1)>),
##  (2, <Success: 2>),
##  (3, <Success: 3>),
##  (4, <Success: 4>)]
