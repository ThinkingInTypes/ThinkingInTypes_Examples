# example_13.py
from typing import LiteralString


def run_query(query: LiteralString): ...


run_query("SELECT * FROM users")  # OK, literal
q = "DROP TABLE users"
# type checker error (q is not literal):
run_query(q)  # type: ignore
