# example_18.py
from typing import Any, cast

request = {"method": "POST", "payload": {"id": 42}}

match request:
    case {"method": m, "payload": data} if (
            m == "POST" and "id" in data
    ):
        data = cast(dict[str, Any], data)
        print(f"POST request with id {data['id']}")

    case {"method": m}:
        print(f"Other request method: {m}")
## POST request with id 42
