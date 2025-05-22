from character.game_character import GameCharacter

class HeroBuilder:
    def __init__(self):
        self.character = GameCharacter()

    def set_name(self, name: str):
        self.character.name = name
        return self

    def set_height(self, height: str):
        self.character.height = height
        return self

    def set_build(self, build: str):
        self.character.build = build
        return self

    def set_hair_color(self, hair_color: str):
        self.character.hair_color = hair_color
        return self

    def set_eye_color(self, eye_color: str):
        self.character.eye_color = eye_color
        return self

    def set_clothing(self, clothing: str):
        self.character.clothing = clothing
        return self

    def add_inventory(self, item: str):
        self.character.inventory.append(item)
        return self

    def add_good_deed(self, deed: str):
        self.character.good_deeds.append(deed)
        return self

    def build(self):
        return self.character
