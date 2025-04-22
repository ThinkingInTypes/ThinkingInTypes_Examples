# composing_functions_demo.py
from pprint import pprint
from composing_functions import composed

pprint([(i, composed(i)) for i in range(5)])
## [(0, <Failure: division by zero>),
##  (1, <Failure: func_a(1)>),
##  (2, <Failure: func_b(2)>),
##  (3, <Failure: func_c(3): division by zero>),
##  (4, <Success: func_d(1): 1>)]
