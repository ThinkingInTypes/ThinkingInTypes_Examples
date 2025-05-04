# smalltalk_parrot.py
from dataclasses import dataclass, field
from types import MethodType


@dataclass
class Parrot:
    known_phrases: list[str] = field(default_factory=list)
    _dynamic_methods: set[str] = field(default_factory=set, init=False, repr=False)

    def __getattr__(self, name: str):
        def handler(*args, **kwargs):
            return self.does_not_understand(name, *args, **kwargs)

        return handler

    def __dir__(self) -> list[str]:
        return sorted(set(super().__dir__()) | self._dynamic_methods)

    def does_not_understand(self, message: str, *args, **kwargs):
        print(f"[Class] Parrot learns new phrase: {message}")

        def new_method(self, *args, **kwargs):
            print(f"Parrot says: {message}")
            self.known_phrases.append(message)

        setattr(self.__class__, message, new_method)
        self._dynamic_methods.add(message)

        return getattr(self, message)(*args, **kwargs)
