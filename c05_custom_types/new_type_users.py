# new_type_users.py
from typing import NewType

UserID = NewType("UserID", int)
ProductID = NewType("ProductID", int)
Users = NewType("Users", list[UserID])

users = Users([UserID(2), UserID(5), UserID(42)])


def increment(uid: UserID) -> UserID:
    # Transparently access underlying value:
    return UserID(uid + 1)


# increment(42)  # Type check error

# Access underlying list operation:
print(increment(users[-1]))


## 43


def increment_users(users: Users) -> Users:
    return Users([increment(uid) for uid in users])


print(increment_users(users))
## [3, 6, 43]
