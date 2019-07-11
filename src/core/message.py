from enum import Enum


class MessageType(Enum):
    TEXT = "TEXT"
    IMAGE = "IMAGE"


class Message(object):
    message_type = None
    content = None

    def show_content(self, func=None):
        pass


class TextMessage(Message):
    def __init__(self, content):
        self.message_type = MessageType.TEXT
        self.content = content

    def show_content(self, func=None):
        if func:
            return func(self.content)
        else:
            return self.content


class ImageMessage(Message):
    def __init__(self, content):
        self.message_type = MessageType.IMAGE
        self.content = content

    def show_content(self, func=None):
        if func:
            return func(self.content)
        else:
            return self.content
