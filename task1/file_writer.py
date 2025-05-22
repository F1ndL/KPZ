class FileWriter:
    def __init__(self, filename):
        self.filename = filename

    def Write(self, message):
        with open(self.filename, "a", encoding="utf-8") as file:
            file.write(message)

    def WriteLine(self, message):
        with open(self.filename, "a", encoding="utf-8") as file:
            file.write(message + "\n")
