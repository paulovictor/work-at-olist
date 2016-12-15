
class FormatError(Exception):
    def __init__(self, message):
        self.strerror = message
