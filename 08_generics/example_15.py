# example_15.py
from drawable import Drawable

def render(item: Drawable) -> None:
    item.draw()

# Example classes that satisfy the protocol:
class Circle:
    def draw(self) -> None:
        print("Drawing a circle")

class Text:
    def draw(self) -> None:
        print("Rendering text")

circle = Circle()
text = Text()
render(circle)  # OK, Circle has draw()
render(text)    # OK, Text has draw()
# render(123)   # type checker error: int has no draw()
