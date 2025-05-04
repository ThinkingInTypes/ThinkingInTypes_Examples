# chatbot.py
from smalltalk_object import SmalltalkObject


class Chatbot(SmalltalkObject):
    def __init__(self):
        self.history = []
