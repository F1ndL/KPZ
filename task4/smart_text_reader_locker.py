import re
from smart_text_reader import SmartTextReader

class SmartTextReaderLocker:
    def __init__(self, smart_text_reader: SmartTextReader, pattern: str):
        self.smart_text_reader = smart_text_reader
        self.pattern = pattern

    def read(self):
        if re.search(self.pattern, self.smart_text_reader.filename):
            print("Access denied!")
            return []
        else:
            return self.smart_text_reader.read()
