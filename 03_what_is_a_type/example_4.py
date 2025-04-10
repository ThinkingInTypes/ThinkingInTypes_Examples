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
studebaker = Car()
quacks(donald)  # Quack!
## Quack!
quacks(studebaker)   # I can quack, too!
## I can quack, too!
