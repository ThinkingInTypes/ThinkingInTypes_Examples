# dynamic_class_creation.py

BaseAnimal = type(
    "BaseAnimal",  # name
    (object,),  # bases
    {  # class body (attributes/methods)
        "speak": lambda self: print("Generic animal sound.")
    }
)

Cat = type(  # Subclassing
    "Cat",
    (BaseAnimal,),
    {
        "speak": lambda self: print("Meow!")
    }
)

feline = Cat()
feline.speak()  # type: ignore
## Meow!
