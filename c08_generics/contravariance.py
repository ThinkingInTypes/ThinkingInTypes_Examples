# contravariance.py
from typing import Generic, TypeVar

from animals import Animal, Dog

T_contra = TypeVar("T_contra", contravariant=True)


class Sink(Generic[T_contra]):
    def send(self, value: T_contra) -> None:
        print(f"Processing {value}")


animal_sink: Sink[Animal] = Sink()
# Contravariance in action:
dog_sink: Sink[Dog] = animal_sink  # type: ignore # Pycharm
# dog_sink expects at least Dog, and Animal is broader:
dog_sink.send(Dog())
## Processing Dog(name=None)
