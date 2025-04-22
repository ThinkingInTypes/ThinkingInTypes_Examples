# duck_typing.py
class Duck:
    def quack(self):
        print("Quack!")


class Car:
    def quack(self):
        print("I can quack, too!")


def quacks(entity):
    entity.quack()
