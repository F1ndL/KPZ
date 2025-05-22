class SmartTextReader:
    def __init__(self, filename: str):
        self.filename = filename

    def read(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                lines = file.readlines()
            array = [list(line.rstrip("\n")) for line in lines]
            return array
        except Exception as e:
            print(f"Помилка: {e}")
            return []
