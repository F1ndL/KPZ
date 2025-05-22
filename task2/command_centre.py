class CommandCentre:
    def __init__(self):
        self.runway = None

    def set_runway(self, runway):
        self.runway = runway

    def request_landing(self, aircraft):
        print(f"CommandCentre: Отримано запит на посадку від {aircraft.name}.")
        if self.runway is None:
            print("CommandCentre: Злітно-посадкова смуга відсутня!")
            return

        if self.runway.is_available():
            print(f"CommandCentre: Смуга {self.runway.name} вільна. {aircraft.name} може приземлятися.")
            self.runway.land(aircraft)
        else:
            print(f"CommandCentre: Смуга {self.runway.name} зайнята. {aircraft.name}, будь ласка, зачекайте.")
