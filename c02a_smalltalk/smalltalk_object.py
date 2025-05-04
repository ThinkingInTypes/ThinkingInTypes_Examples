# smalltalk_object.py
class SmalltalkObject:
    def __getattr__(self, name):
        def handler(*args, **kwargs):
            return self.not_found(name, *args, **kwargs)

        return handler

    def not_found(self, message, *args, **kwargs):
        print(
            f"{self.__class__.__name__}: '{message}' not found"
        )
