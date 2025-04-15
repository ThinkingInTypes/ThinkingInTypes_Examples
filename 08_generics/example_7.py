# example_7.py
from typing import Generic, TypeVar
from animals import Animal, Dog

T_contra = TypeVar('T_contra', contravariant=True)

class Sink(Generic[T_contra]):
    def send(self, value: T_contra) -> None:
        print(f"Processing {value}")

animal_sink: Sink[Animal] = Sink()
dog_sink: Sink[Dog] = animal_sink   # This is OK because of contravariance
dog_sink.send(Dog())               # Safe: dog_sink expects at least Dog, and Animal is broader
