from smart_text_reader import SmartTextReader

class SmartTextChecker:
    def __init__(self, smart_text_reader: SmartTextReader):
        self.smart_text_reader = smart_text_reader

    def read(self):
        print(f"Відкриття файлу: {self.smart_text_reader.filename}")
        data = self.smart_text_reader.read()
        print("Файл успішно прочитано.")
        total_lines = len(data)
        total_chars = sum(len(line) for line in data)
        print(f"Загальна кількість рядків: {total_lines}, символів: {total_chars}")
        print("Закриття файлу.")
        return data
