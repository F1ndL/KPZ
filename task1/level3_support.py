from handler import Handler

class Level3Support(Handler):
    def handle(self):
        print("\n--- Третій рівень підтримки: Підтримка з питань оплати ---")
        answer = input("Введіть '3' для підтримки з питань оплати, або натисніть Enter для переходу до наступного рівня: ")
        if answer == '3':
            print("Ви обрали підтримку з питань оплати.")
            return True
        elif self.next_handler:
            return self.next_handler.handle()
        else:
            return False
