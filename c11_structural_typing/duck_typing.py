# duck_typing.py


class Duck:
    def walk(self): ...
    def quack(self): ...


class Robot:
    def walk(self): ...
    def quack(self): ...


def be_a_duck(duck):
    duck.walk()
    duck.quack()


be_a_duck(Duck())
be_a_duck(Robot())
