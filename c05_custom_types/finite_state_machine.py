# finite_state_machine.py
from enum import Enum

class Event(Enum):
  SUBMIT = "submit"
  APPROVE = "approve"
  REJECT = "reject"
  REOPEN = "reopen"

class Status(Enum):
  OPEN = "open"
  PENDING = "pending"
  CLOSED = "closed"

  _initialized: ClassVar[bool] = False

  def __init__(self, label: str):
    self._label = label
    self._transitions: dict[Event, Status] = {}

  def on_event(self, event: Event) -> "Status":
    if not self._initialized:
      type(self).initialize_transitions()
    next_state = self._transitions.get(event)
    if next_state is None:
      print(f"No valid transition from {self.name} on event {event.name!r}. Staying in {self.name}.")
      return self
    print(f"{self.name} + {event.name!r} → {next_state.name}")
    return next_state

  @property
  def label(self) -> str:
    return self._label

  @classmethod
  def initialize_transitions(cls) -> None:
    if cls._initialized:
      return  # Prevent double init
    transitions: dict[Status, dict[Event, Status]] = {
      cls.OPEN: {
        Event.SUBMIT: cls.PENDING,
      },
      cls.PENDING: {
        Event.APPROVE: cls.CLOSED,
        Event.REJECT: cls.OPEN,
      },
      cls.CLOSED: {
        Event.REOPEN: cls.OPEN,
      },
    }
    for state, mapping in transitions.items():
      state._transitions = mapping
    cls._initialized = True

def run(initial: Status, events: list[Event]) -> None:
  state = initial
  print(f"Starting at {state.label}")
  for event in events:
    state = state.on_event(event)
    print(f"Now at {state.label}")

workflow = [
  Event.SUBMIT,
  Event.REJECT,
  Event.SUBMIT,
  Event.APPROVE,
  Event.REOPEN,
]

run(Status.OPEN, workflow)
