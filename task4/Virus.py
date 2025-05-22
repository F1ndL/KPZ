class Virus:
    def __init__(self, weight: float, age: float, name: str, species: str):
        self.weight = weight      # вага
        self.age = age            # вік
        self.name = name          # ім’я
        self.species = species    # вид
        self.children = []        # список дітей (екземпляри Virus)

    def add_child(self, child: "Virus") -> None:
        self.children.append(child)

    def clone(self) -> "Virus":
        cloned = Virus(self.weight, self.age, self.name, self.species)
        cloned.children = [child.clone() for child in self.children]
        return cloned

    def display(self, level: int = 0) -> None:
        indent = "  " * level
        print(f"{indent}Virus: {self.name}, Species: {self.species}, Age: {self.age}, Weight: {self.weight}")
        for child in self.children:
            child.display(level + 1)