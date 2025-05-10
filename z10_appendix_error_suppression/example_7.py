# example_7.py
class Server:
    def accept(self):
        self.socket = object()  # imagine this is set in listen()
        return self.socket.recv()  # pytype: disable=attribute-error # type: ignore # noqa
