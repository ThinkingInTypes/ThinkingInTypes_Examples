class Person:
    def __init__(self, name: str):
        self.name = name


class Animal:
    def __init__(self, name: str):
        self.name = name


# Type checker: Expected type 'Person', got 'Animal' instead
person: Person = Animal("Bob")
print(isinstance(person, Person))  # False
print(isinstance(person, Animal))  # True
