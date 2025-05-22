class Hero:
    def get_description(self):
        return "Герой без імені"


class Warrior(Hero):
    def get_description(self):
        return "Warrior"


class Mage(Hero):
    def get_description(self):
        return "Mage"


class Palladin(Hero):
    def get_description(self):
        return "Palladin"
