# example_8.py


class Box[T]:
    def __init__(self, content: T):
        self.content = content

    def get_content(self) -> T:
        return self.content
