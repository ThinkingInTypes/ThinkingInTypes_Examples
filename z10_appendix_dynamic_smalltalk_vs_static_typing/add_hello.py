# add_hello.py
from chatbot import Chatbot

bot = Chatbot()


def hello(self):
    print("Hello! I'm your chatbot.")
    self.history.add("hello")


setattr(Chatbot, "hello", hello)
bot.hello()
## Hello! I'm your chatbot.
