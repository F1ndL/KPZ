from builders.enemy_builder import EnemyBuilder

class EnemyDirector:
    def __init__(self, builder: EnemyBuilder):
        self.builder = builder

    def construct(self):
        return (self.builder
                .set_name("Lord Umbra")
                .set_height("185 cm")
                .set_build("Heavy and imposing")
                .set_hair_color("Black")
                .set_eye_color("Red")
                .set_clothing("Dark Armor")
                .add_inventory("Cursed Blade")
                .add_inventory("Toxic Elixir")
                .add_evil_deed("Destroyed a kingdom")
                .add_evil_deed("Plundered sacred temples")
                .build())
