# state_machine.py
from enum import Enum

def open_next(self) -> "Status":
  print("Moving from OPEN to PENDING.")
  return Status.PENDING

def pending_next(self) -> "Status":
  print("Moving from PENDING to CLOSED.")
  return Status.CLOSED

def closed_next(self) -> "Status":
  print("CLOSED is a final state. Staying put.")
  return Status.CLOSED

class Status(Enum):
  OPEN = ("open", open_next)
  PENDING = ("pending", pending_next)
  CLOSED = ("closed", closed_next)

  def __init__(self, label: str, next_handler: callable):
    self._label = label
    self._next_handler = next_handler

  def next(self) -> "Status":
    return self._next_handler(self)

  @property
  def label(self) -> str:
    return self._label


def start(state: Status = Status.OPEN):
  while(state != Status.CLOSED):
    print(state.label)
    state = state.next()
