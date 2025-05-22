from hero import Warrior, Mage, Palladin
from hero_decorator import ClothingDecorator, WeaponDecorator, ArtifactDecorator


def main():
    warrior = Warrior()
    warrior = ClothingDecorator(warrior, "шкіряною бронею")
    warrior = WeaponDecorator(warrior, "мечем долі")
    warrior = ArtifactDecorator(warrior, "амулетом сили")
    print("Warrior:")
    print(warrior.get_description())
    print("-" * 50)

    mage = Mage()
    mage = ClothingDecorator(mage, "чарівною мантією")
    mage = WeaponDecorator(mage, "палицею мудрості")
    mage = WeaponDecorator(mage, "кинджалом тіні")
    mage = ArtifactDecorator(mage, "кілець мани")
    print("Mage:")
    print(mage.get_description())
    print("-" * 50)

    palladin = Palladin()
    palladin = ClothingDecorator(palladin, "плащем відваги")
    palladin = WeaponDecorator(palladin, "блакитним молотом")
    palladin = ArtifactDecorator(palladin, "щитком відвертості")
    print("Palladin:")
    print(palladin.get_description())


if __name__ == "__main__":
    main()
