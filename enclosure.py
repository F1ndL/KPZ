class Enclosure:
    def __init__(self, enclosure_id, size, enclosure_type):
        self.enclosure_id = enclosure_id
        self.size = size
        self.enclosure_type = enclosure_type
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def get_animals(self):
        return [a.get_info() for a in self.animals]