# example_2.py
class Duck:
    # noinspection PyMethodMayBeStatic
    def quack(self):
        print("Quack!")


def make_it_quack(bird):
    bird.quack()


make_it_quack(Duck())  # works fine
## Quack!
