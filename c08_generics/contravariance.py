# contravariance.py
from typing import Generic, TypeVar
from animals import Animal, Dog

## Woof
## Woof
## Animal sound

T_contra = TypeVar("T_contra", contravariant=True)


class Sink(Generic[T_contra]):
    def send(self, value: T_contra) -> None:
        print(f"Processing {value}")


animal_sink: Sink[Animal] = Sink()
# Contravariance in action:
dog_sink: Sink[Dog] = animal_sink
# dog_sink expects at least Dog, and Animal is broader:
dog_sink.send(Dog())
## Processing <animals.Dog object at
## 0x00000281C5AFA350>
