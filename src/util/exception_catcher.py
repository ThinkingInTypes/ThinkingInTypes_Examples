# util/exception_catcher.py
from contextlib import contextmanager


@contextmanager
def capture():
    try:
        yield
    except Exception as e:
        print(f"Error: {e}")
