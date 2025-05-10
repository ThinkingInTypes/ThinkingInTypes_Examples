# example_5.py
foo: int = "123"  # pyright: ignore # noqa
bar: int = "123"  # pyright: ignore [reportGeneralTypeIssues] # type: ignore # noqa
