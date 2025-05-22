from hero import Hero

class HeroDecorator(Hero):
    def __init__(self, hero: Hero):
        self.hero = hero

    def get_description(self):
        return self.hero.get_description()


class ClothingDecorator(HeroDecorator):
    def __init__(self, hero: Hero, clothing: str):
        super().__init__(hero)
        self.clothing = clothing

    def get_description(self):
        return f"{self.hero.get_description()}, одягнений у {self.clothing}"


class WeaponDecorator(HeroDecorator):
    def __init__(self, hero: Hero, weapon: str):
        super().__init__(hero)
        self.weapon = weapon

    def get_description(self):
        return f"{self.hero.get_description()}, озброєний {self.weapon}"


class ArtifactDecorator(HeroDecorator):
    def __init__(self, hero: Hero, artifact: str):
        super().__init__(hero)
        self.artifact = artifact

    def get_description(self):
        return f"{self.hero.get_description()}, володіє {self.artifact}"
