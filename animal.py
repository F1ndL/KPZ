class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def get_info(self):
        return f"{self.name} ({self.species}), {self.age} y.o."

class Mammal(Animal):
    def __init__(self, name, species, age, fur_color):
        super().__init__(name, species, age)
        self.fur_color = fur_color

class Bird(Animal):
    def __init__(self, name, species, age, wing_span):
        super().__init__(name, species, age)
        self.wing_span = wing_span