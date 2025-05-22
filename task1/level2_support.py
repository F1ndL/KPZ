from handler import Handler

class Level2Support(Handler):
    def handle(self):
        print("\n--- Другий рівень підтримки: Технічна підтримка ---")
        answer = input("Введіть '2' для технічної підтримки, або натисніть Enter для переходу до наступного рівня: ")
        if answer == '2':
            print("Ви обрали технічну підтримку.")
            return True
        elif self.next_handler:
            return self.next_handler.handle()
        else:
            return False
