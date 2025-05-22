from text_editor import TextEditor


def main():
    editor = TextEditor()

    print("Початковий вміст документа:")
    print(editor.document.get_content())
    print("-" * 50)

    editor.type_text("Привіт, світ!\n")
    editor.save()

    editor.type_text("Це другий рядок тексту.\n")
    print("Вміст документа після змін:")
    print(editor.document.get_content())
    print("-" * 50)

    editor.undo()
    print("Вміст документа після скасування змін:")
    print(editor.document.get_content())


if __name__ == "__main__":
    main()
