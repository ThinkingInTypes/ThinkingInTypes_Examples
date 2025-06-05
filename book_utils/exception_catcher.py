# book_utils/exception_catcher.py
"""
Context manager that catches exceptions and prints their error messages,
and can be used as a callable via its __call__ method.

When used as a callable, argument evaluation must be delayed until inside
the context manager in case argument evaluation raises an exception.
To do this the function should be provided as a zero-argument callable.
If the function takes arguments, it must be wrapped in a lambda to delay evaluation.
"""

import traceback as _traceback
from typing import Any, Callable

_NO_REPORT = ["# type: ignore", "# noqa"]


class Catch:
    """
    Catch and print expected errors, but allow _fatal_exceptions to propagate.
    Lines annotated with any marker in _NO_REPORT are not reported.
    """

    _fatal_exceptions = (
        SyntaxError,
        NameError,
        TypeError,
        AttributeError,
    )

    def __enter__(self) -> Catch:
        return self

    def __exit__(
        self, exc_type: Any, exc_value: Any, tb: Any
    ) -> bool:
        if exc_type is None:
            return True

        if self._is_ignored_frame(tb):
            return True

        if issubclass(exc_type, self._fatal_exceptions):
            return False

        print(f"Error: {exc_value}")
        return True

    def __call__[R](self, func: Callable[[], R]) -> R | None:
        try:
            result = func()
            if result is not None:
                print(result)
            return result
        except Exception as e:
            if self._is_ignored_frame(e.__traceback__):
                return None

            if isinstance(e, self._fatal_exceptions):
                raise

            print(f"Error: {e}")
            return None

    def _is_ignored_frame(self, tb: Any) -> bool:
        frames = (
            _traceback.extract_tb(tb) if tb is not None else []
        )
        return any(
            any(tag in (frame.line or "") for tag in _NO_REPORT)
            for frame in frames
        )
