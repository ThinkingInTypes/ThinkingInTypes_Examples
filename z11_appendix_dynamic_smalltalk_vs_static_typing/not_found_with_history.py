# not_found_with_history.py


def not_found(self, message, *args, **kwargs):
    print(f"Don't know '{message}'; remembering it.")
    self.history.add(message)
