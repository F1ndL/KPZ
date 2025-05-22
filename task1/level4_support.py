from handler import Handler

class Level4Support(Handler):
    def handle(self):
        print("\n--- Четвертий рівень підтримки: Ескалація до менеджера ---")
        answer = input("Введіть '4' для ескалації до менеджера, або натисніть Enter для завершення: ")
        if answer == '4':
            print("Ви обрали ескалацію до менеджера.")
            return True
        else:
            return False
