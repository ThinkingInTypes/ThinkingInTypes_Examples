# accidental_genericity.py
global_var = None


# warning: TypeVar "T" appears only     │
# once in generic function signature
def set_value[T](x: T) -> None:  # type: ignore
    global global_var
    global_var = x
