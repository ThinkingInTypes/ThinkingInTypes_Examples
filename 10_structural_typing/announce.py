# announce.py
from speaker import Speaker


class Dog:
    def speak(self) -> str:
        return "woof"


class Robot:
    def speak(self) -> str:
        return "beep-boop"


def announce(speaker: Speaker) -> None:
    # `speaker` can be any object that has .speak() returning str
    print("Announcement:", speaker.speak())


announce(Dog())  # OK, Dog has speak()
## Announcement: woof
announce(Robot())  # OK, Robot has speak()
## Announcement: beep-boop
