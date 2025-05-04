# override_not_found.py
from chatbot import Chatbot
from talk_to_chatbot import bot


def not_found(self, message, *args, **kwargs):
    print(f"Sorry, I don't understand '{message}', but I'll remember it.")
    self.history.append(message)


setattr(Chatbot, "not_found", not_found)

bot.weather()
bot.joke()
