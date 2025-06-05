# smalltalk_object.py


class SmalltalkObject:
    def __getattr__(self, name):
        def handler(*args, **kwargs):
            return self.not_found(name, *args, **kwargs)

        return handler

    def not_found(self, message, *args, **kwargs):
        args_str = ", ".join(repr(arg) for arg in args)
        kwargs_str = ", ".join(
            f"{k}={v!r}" for k, v in kwargs.items()
        )
        all_args = ", ".join(
            filter(None, [args_str, kwargs_str])
        )

        print(
            f"{self.__class__.__name__}: {message}({all_args}) not found"
        )
