# override_not_found.py
from chatbot import Chatbot
from not_found_with_history import not_found

bot = Chatbot()
setattr(Chatbot, "not_found", not_found)

bot.weather()
## Don't know 'weather'; remembering it.
bot.joke()
## Don't know 'joke'; remembering it.
bot.weather()
bot.joke()
