# main.py
from level1_support import Level1Support
from level2_support import Level2Support
from level3_support import Level3Support
from level4_support import Level4Support


def main():
    handler4 = Level4Support()
    handler3 = Level3Support(next_handler=handler4)
    handler2 = Level2Support(next_handler=handler3)
    handler1 = Level1Support(next_handler=handler2)

    print("Система підтримки користувачів\n")

    while True:
        if handler1.handle():
            print("\nЗвернення успішно оброблено!")
            break
        else:
            print("\nНе вдалося визначити потрібний рівень підтримки. Будь ласка, спробуйте ще раз.\n")


if __name__ == "__main__":
    main()
