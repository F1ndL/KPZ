from builders.hero_builder import HeroBuilder

class HeroDirector:
    def __init__(self, builder: HeroBuilder):
        self.builder = builder

    def construct(self):
        return (self.builder
                .set_name("Lady Aurora")
                .set_height("170 cm")
                .set_build("Slim and agile")
                .set_hair_color("Red")
                .set_eye_color("Green")
                .set_clothing("Mystic Robe")
                .add_inventory("Magic Wand")
                .add_inventory("Healing Potion")
                .add_good_deed("Rescued villagers")
                .add_good_deed("Healed the sick")
                .build())
