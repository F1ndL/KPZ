class Aircraft:
    def __init__(self, name, mediator):
        self.name = name
        self.mediator = mediator

    def request_landing(self):
        print(f"Aircraft {self.name}: Відправляю запит на посадку.")
        self.mediator.request_landing(self)
