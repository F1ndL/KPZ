class ZooInventory:
    def __init__(self):
        self.animals = []
        self.enclosures = []
        self.foods = []
        self.workers = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_enclosure(self, enclosure):
        self.enclosures.append(enclosure)

    def add_food(self, food):
        self.foods.append(food)

    def add_worker(self, worker):
        self.workers.append(worker)

    def print_summary(self):
        print(f"Total animals: {len(self.animals)}")
        print(f"Total enclosures: {len(self.enclosures)}")
        print(f"Total food types: {len(self.foods)}")
        print(f"Total workers: {len(self.workers)}")