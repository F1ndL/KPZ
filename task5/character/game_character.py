class GameCharacter:
    def __init__(self):
        self.name = ""
        self.height = ""
        self.build = ""
        self.hair_color = ""
        self.eye_color = ""
        self.clothing = ""
        self.inventory = []
        self.good_deeds = []  # Список добрих вчинків (для героя)
        self.evil_deeds = []  # Список злих вчинків (для ворога)

    def __str__(self):
        result = f"Name: {self.name}\n"
        result += f"Height: {self.height}\n"
        result += f"Build: {self.build}\n"
        result += f"Hair Color: {self.hair_color}\n"
        result += f"Eye Color: {self.eye_color}\n"
        result += f"Clothing: {self.clothing}\n"
        result += f"Inventory: {', '.join(self.inventory)}\n"
        if self.good_deeds:
            result += f"Good Deeds: {', '.join(self.good_deeds)}\n"
        if self.evil_deeds:
            result += f"Evil Deeds: {', '.join(self.evil_deeds)}\n"
        return result
