# smalltalk_parrot.py
from dataclasses import dataclass, field


@dataclass
class Parrot:
    known_phrases: list[str] = field(default_factory=list)

    def __getattr__(self, name: str):
        def handler(*args, **kwargs):
            return self.not_found(name, *args, **kwargs)

        return handler

    def not_found(self, message: str, *args, **kwargs):
        print(f"[Class] Parrot learns: {message}")

        def new_method(self, *args, **kwargs):
            print(f"Parrot says: {message}")
            self.known_phrases.append(message)

        setattr(self.__class__, message, new_method)
        return getattr(self, message)(*args, **kwargs)
