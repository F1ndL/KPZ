class Runway:
    def __init__(self, name):
        self.name = name
        self.available = True

    def is_available(self):
        return self.available

    def land(self, aircraft):
        print(f"Runway {self.name}: {aircraft.name} здійснює посадку.")
        self.available = False
        print(f"Runway {self.name}: {aircraft.name} успішно приземлився. Смуга тепер вільна.")
        self.available = True
