# star_demo.py
from stars import Stars
from book_utils import Catch


def f1(s: Stars) -> Stars:
    return Stars(s.number + 5)


def f2(s: Stars) -> Stars:
    return Stars(s.number * 5)


stars1 = Stars(4)
print(stars1)
## Stars(number=4)

print(f1(stars1))
## Stars(number=9)
with Catch():
    print(f2(f1(stars1)))
## Error: Stars(number=45)
with Catch():
    stars2 = Stars(11)
## Error: Stars(number=11)
with Catch():
    print(f1(Stars(11)))
## Error: Stars(number=11)
