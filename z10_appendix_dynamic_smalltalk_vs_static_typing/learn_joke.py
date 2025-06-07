# learn_joke.py
from chatbot import Chatbot
from joke import joke

bot = Chatbot()
setattr(Chatbot, "joke", joke)
bot.joke()
## Why did the duck cross the road?
## It was the chicken's day off.
