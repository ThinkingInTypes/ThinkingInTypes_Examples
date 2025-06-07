# introspection.py
from add_hello import bot
## Hello! I'm your chatbot.

print([m for m in dir(bot) if not m.startswith("_")])
## ['hello', 'history', 'not_found']
print(bot.history)
## {'hello'}
