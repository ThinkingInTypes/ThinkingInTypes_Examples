# int_stars.py
# Using 1-10 stars for customer feedback.

def f1(stars: int) -> int:
    # Must check argument...
    assert 1 <= stars <= 10, f"f1: {stars}"
    return stars + 5

def f2(stars: int) -> int:
    # ...each place it is used.
    assert 1 <= stars <= 10, f"f2: {stars}"
    return stars * 5

stars1 = 6
print(stars1)
print(f1(stars1))
print(f2(stars1))
stars2 = 11
print(f1(stars2))
stars1 = 99
print(f2(stars1))
