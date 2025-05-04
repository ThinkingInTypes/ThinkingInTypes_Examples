# learning_parrot.py
from smalltalk_parrot import Parrot

polly = Parrot()
coco = Parrot()

# Before learning:
print(polly.known_phrases, coco.known_phrases)
## set() set()

polly.hello()
## [Class] Parrot learns: hello
## Parrot says: hello
coco.hello()
## Parrot says: hello
coco.squawk()
## [Class] Parrot learns: squawk
## Parrot says: squawk

# After learning:
print(polly.known_phrases, coco.known_phrases)
## {'hello'} {'hello', 'squawk'}
