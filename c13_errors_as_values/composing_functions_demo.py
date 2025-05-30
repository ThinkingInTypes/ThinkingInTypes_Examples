# composing_functions_demo.py
from pprint import pprint
from composing_functions import composed

pprint([(i, composed(i)) for i in range(5)])
## [(0, <Failure: division by zero>),
##  (1, <Failure: fa(1)>),
##  (2, <Failure: fb(2)>),
##  (3, <Failure: fc(3): division by zero>),
##  (4, <Success: fd(1): 1>)]
