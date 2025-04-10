# example_4.py
class Duck:
    def quack(self):
        print("Quack!")

class Car:
    def quack(self):
        print("I can quack, too!")

def quacks(entity):
    entity.quack()

donald = Duck()
tesla = Car()
quacks(donald)  # Quack!
## Quack!
quacks(tesla)   # I can quack, too!
## I can quack, too!
