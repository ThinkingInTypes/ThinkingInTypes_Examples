# recursive_alias.py
JSON = (
    dict[str, "JSON"]
    | list["JSON"]
    | str
    | int
    | float
    | bool
    | None
)
