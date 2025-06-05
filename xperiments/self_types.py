class Car:
    def set_brand(self, brand: str) -> Car:
        self.brand = brand
        return self


# call set_brand method
Car().set_brand("Maruti")
print()
