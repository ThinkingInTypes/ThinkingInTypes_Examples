# duck_typing_demo.py
from duck_typing import Duck, Car, quacks

donald = Duck()
studebaker = Car()
quacks(donald)
## Quack!
quacks(studebaker)
## I can quack, too!
