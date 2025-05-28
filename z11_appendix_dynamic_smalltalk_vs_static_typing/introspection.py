# introspection.py
from add_hello import bot
## Hello! I'm your chatbot.
import override_not_found
## Don't know 'weather'; remembering it.
## Don't know 'joke'; remembering it.
import learn_joke

## Why did the duck cross the road?
## It was the chicken's day off.

print([m for m in dir(bot) if not m.startswith("_")])
## ['hello', 'history', 'joke', 'not_found']
print(bot.history)
## {'hello'}
