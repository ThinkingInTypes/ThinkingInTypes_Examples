# optional_typed_dict_fields.py
from typing import TypedDict, NotRequired


class UserSettings(TypedDict):
    theme: str
    notifications_enabled: NotRequired[bool]


# Only the required field is provided:
tettings: UserSettings = {"theme": "dark"}
