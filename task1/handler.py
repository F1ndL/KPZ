class Handler:
    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    def handle(self):
        raise NotImplementedError("Метод handle() повинен бути реалізований у підкласі.")
