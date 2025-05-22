from Virus import Virus

def main():
    grandparent = Virus(0.1, 1.0, "Virus_A", "Alpha")

    parent1 = Virus(0.05, 0.5, "Virus_B", "Beta")
    parent2 = Virus(0.06, 0.5, "Virus_C", "Gamma")

    child1 = Virus(0.02, 0.2, "Virus_D", "Delta")
    child2 = Virus(0.03, 0.2, "Virus_E", "Epsilon")

    grandchild1 = Virus(0.01, 0.1, "Virus_F", "Zeta")

    parent1.add_child(child1)
    parent1.add_child(child2)
    child1.add_child(grandchild1)

    grandparent.add_child(parent1)
    grandparent.add_child(parent2)

    print("Оригінальне сімейне дерево вірусів:")
    grandparent.display()

    cloned_family = grandparent.clone()
    print("\nКлоноване сімейне дерево вірусів:")
    cloned_family.display()


if __name__ == "__main__":
    main()