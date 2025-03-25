# example_2.py
class Stars:
    def __init__(self, stars: int):
        assert 1 <= stars <= 10, "Stars rating must be between 1 and 10."
        self._stars = stars

    @property
    def stars(self):
        return self._stars
