# new_type.py
from typing import NewType

UserID = NewType("UserID", int)
IDs = NewType("IDs", list[UserID])

user_ids = IDs([UserID(2), UserID(5), UserID(42)])


def increment(uid: UserID) -> UserID:
    # Transparently access underlying value:
    return UserID(uid + 1)


# increment(42)  # Type check error

# Access underlying list operation:
print(increment(user_ids[-1]))
## 43


def increment_users(user_ids: IDs) -> IDs:
    return IDs([increment(uid) for uid in user_ids])


print(increment_users(user_ids))
## [3, 6, 43]
