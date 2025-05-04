# add_hello.py
from chatbot import Chatbot
from talk_to_chatbot import bot


def hello(self):
    print("Hello! I'm your chatbot.")
    self.history.append("hello")


setattr(Chatbot, "hello", hello)
bot.hello()
