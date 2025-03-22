# it_all_goes_wrong.py


class A:
    x: int = 100
    y: int = 200

    @classmethod
    def change_x(cls):
        cls.x = 999

    @classmethod
    def change_y(cls):
        cls.y = 313


def reset():
    A.x = 100
    A.y = 200


a1: A = None
a2: A = None
a3: A = None

def display(counter: int):
    print(f"display({counter})")
    if a1:
        print(f"{a1.x = }, {a1.y = }")
    if a2:
        print(f"{a2.x = }, {a2.y = }")
    if a3:
        print(f"{a3.x = }, {a3.y = }")

a1 = A()
display(1)
a1.x = -1
a1.y = -2
display(2)
a1.change_x()
display(3)
a2 = A()
display(4)
a2.y = 17
display(5)
A.change_y()
a3 = A()
display(6)
reset()
display(7)
