from memento import Memento

class TextDocument:
    def __init__(self):
        self._content = ""

    def append_text(self, text: str):
        self._content += text

    def get_content(self) -> str:
        return self._content

    def set_content(self, content: str):
        self._content = content

    def create_memento(self) -> Memento:
        return Memento(self._content)

    def restore_from_memento(self, memento: Memento):
        self._content = memento.get_state()
