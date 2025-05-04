# introspection.py
from add_hello import bot
import override_not_found
import learn_joke

print([m for m in dir(bot) if not m.startswith("_")])
print(bot.history)
