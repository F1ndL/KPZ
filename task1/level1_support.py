from handler import Handler

class Level1Support(Handler):
    def handle(self):
        print("\n--- Перший рівень підтримки: Базова підтримка ---")
        answer = input("Введіть '1' для базової підтримки, або натисніть Enter для переходу до наступного рівня: ")
        if answer == '1':
            print("Ви обрали базову підтримку.")
            return True
        elif self.next_handler:
            return self.next_handler.handle()
        else:
            return False
