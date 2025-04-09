# example_9.py
from book_utils import Catch
from example_8 import Rectangle

r = Rectangle(3.0, 4.0)
print(r.area)  # Outputs: 12.0
## 12.0
# Try to modify attributes (should fail)
with Catch():
    # 'Rectangle' object attribute 'width' is read-only:
    # r.width = 5.0
    r.__dict__["width"] = 5.0  # Cheat to change
