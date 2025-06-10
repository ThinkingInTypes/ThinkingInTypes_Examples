# announce.py
from dataclasses import dataclass

from speaker import Speaker


@dataclass
class Dog:
    def speak(self) -> str:
        return "woof"


@dataclass
class Robot:
    def speak(self) -> str:
        return "beep-boop"


def announce(speaker: Speaker) -> None:
    # `speaker` can be any object with .speak() returning str
    print("Announcement:", speaker.speak())


announce(Dog())  # Dog has speak()
## Announcement: woof
announce(Robot())  # Robot has speak()
## Announcement: beep-boop
