from animal import Mammal, Bird
from enclosure import Enclosure
from food import Food
from worker import ZooWorker
from inventory import ZooInventory

def main():
    zoo = ZooInventory()

    tiger = Mammal("Tigra", "Tiger", 5, "Orange")
    parrot = Bird("Kesha", "Parrot", 2, 0.5)

    enclosure1 = Enclosure(1, "Large", "Savanna")
    enclosure1.add_animal(tiger)

    enclosure2 = Enclosure(2, "Small", "Tropical")
    enclosure2.add_animal(parrot)

    meat = Food("Meat", 50, "Tiger")
    seeds = Food("Seeds", 10, "Parrot")

    worker1 = ZooWorker("Ivan", "Keeper")
    worker2 = ZooWorker("Olena", "Vet")

    zoo.add_animal(tiger)
    zoo.add_animal(parrot)
    zoo.add_enclosure(enclosure1)
    zoo.add_enclosure(enclosure2)
    zoo.add_food(meat)
    zoo.add_food(seeds)
    zoo.add_worker(worker1)
    zoo.add_worker(worker2)

    zoo.print_summary()

if __name__ == "__main__":
    main()