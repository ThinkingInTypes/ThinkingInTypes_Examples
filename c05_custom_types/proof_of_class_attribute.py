# proof_of_class_attribute.py

class A:
    x: int = 1

    def show(self) -> None:
        class_x = getattr(self.__class__, "x", "<not found>")
        print(
            f"A.x = {class_x}  "
            f"a.__dict__  = {self.__dict__}  "
            f"a.x = {getattr(self, "x", "<not found>")}"
        )


a = A()
a.show()
## A.x = 1  a.__dict__  = {}  a.x = 1
a.x = 2
a.show()
## A.x = 1  a.__dict__  = {'x': 2}  a.x = 2
