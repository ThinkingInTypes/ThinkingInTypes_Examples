# contravariance.py
from animals import Animal, Dog

class Sink[T]:
    def send(self, value: T) -> None:
        print(f"Processing {value}")


animal_sink: Sink[Animal] = Sink()
# Contravariance in action:
dog_sink: Sink[Dog] = animal_sink  # type: ignore # Pycharm
# dog_sink expects at least Dog, and Animal is broader:
dog_sink.send(Dog())
## Processing Dog(name=None)
