# enum_exhaustivity.py
from enum import Enum

class Status(Enum):
  OPEN = "open"
  CLOSED = "closed"
  PENDING = "pending"

  def handle_status(self) -> str:
    match self:
      case Status.OPEN:
        return "Handling open status."
      case Status.CLOSED:
        return "Handling closed status."
      case Status.PENDING:
        return "Handling pending status."
      # No `case _:` fallback needed if we cover all members!

print(Status.OPEN.handle())   
print(Status.CLOSED.handle()) 
print(Status.PENDING.handle())
