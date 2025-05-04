# learning_parrot.py
from smalltalk_parrot import Parrot

polly = Parrot()
coco = Parrot()

print("Before learning:", [m for m in dir(polly) if not m.startswith('_')])
## Before learning: ['does_not_understand',
## 'known_phrases']

polly.hello()
## [Class] Parrot learns new phrase: hello
## Parrot says: hello
coco.squawk()
## [Class] Parrot learns new phrase: squawk
## Parrot says: squawk

print("After learning:", [m for m in dir(polly) if not m.startswith('_')])
## After learning: ['does_not_understand',
## 'hello', 'known_phrases', 'squawk']
