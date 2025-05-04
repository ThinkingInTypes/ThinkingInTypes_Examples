# learn_joke.py
from chatbot import Chatbot
from add_hello import bot


def joke(self):
    print("Why did the duck cross the road? It was the chicken's day off.")
    self.history.append("joke")


setattr(Chatbot, "joke", joke)
bot.joke()
