from text_document import TextDocument

class TextEditor:
    def __init__(self):
        self.document = TextDocument()
        self._history = []

    def type_text(self, text: str):
        self.document.append_text(text)

    def save(self):
        memento = self.document.create_memento()
        self._history.append(memento)
        print("Стан документа збережено.")

    def undo(self):
        if not self._history:
            print("Немає збережених станів для відновлення.")
            return
        memento = self._history.pop()
        self.document.restore_from_memento(memento)
        print("Операція скасування виконана.")
