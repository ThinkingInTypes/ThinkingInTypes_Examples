# container_types.py

class StringContainer:
    def __init__(self, value: str):
        self.value = value

    def get_item(self) -> str:
        return self.value


class IntContainer:
    def __init__(self, value: int):
        self.value = value

    def get_item(self) -> int:
        return self.value
