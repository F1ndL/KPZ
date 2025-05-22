from file_writer import FileWriter

class FileLogger:
    def __init__(self, filename):
        self.file_writer = FileWriter(filename)

    def Log(self, message):
        self.file_writer.WriteLine("LOG: " + message)

    def Error(self, message):
        self.file_writer.WriteLine("ERROR: " + message)

    def Warn(self, message):
        self.file_writer.WriteLine("WARN: " + message)
