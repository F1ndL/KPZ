from smart_text_reader import SmartTextReader
from smart_text_checker import SmartTextChecker
from smart_text_reader_locker import SmartTextReaderLocker


def main():
    sample_filename = "sample.txt"
    with open(sample_filename, "w", encoding="utf-8") as f:
        f.write("Hello World\nThis is a test\nProxy pattern example")

    print("=== Демонстрація SmartTextChecker (з логуванням) ===")
    reader = SmartTextReader(sample_filename)
    checker = SmartTextChecker(reader)
    data = checker.read()
    print("Результат (двомірний масив символів):")
    print(data)

    print("\n=== Демонстрація SmartTextReaderLocker (обмеження доступу) ===")
    restricted_filename = "secret_file.txt"
    with open(restricted_filename, "w", encoding="utf-8") as f:
        f.write("This is a secret content")

    reader_restricted = SmartTextReader(restricted_filename)
    locker = SmartTextReaderLocker(reader_restricted, r"secret")
    data_locked = locker.read()
    print("Результат:", data_locked)

    print("\n=== Демонстрація SmartTextReaderLocker (дозволений доступ) ===")
    allowed_filename = "allowed_file.txt"
    with open(allowed_filename, "w", encoding="utf-8") as f:
        f.write("This file is allowed")

    reader_allowed = SmartTextReader(allowed_filename)
    locker_allowed = SmartTextReaderLocker(reader_allowed, r"secret")
    data_allowed = locker_allowed.read()
    print("Результат:", data_allowed)


if __name__ == "__main__":
    main()
