from logger import Logger
from file_logger import FileLogger


def main():
    print("Консольний логгер:")
    console_logger = Logger()
    console_logger.Log("Це звичайне повідомлення")
    console_logger.Error("Це повідомлення про помилку")
    console_logger.Warn("Це попереджувальне повідомлення")

    log_file = "log.txt"
    with open(log_file, "w", encoding="utf-8") as f:
        f.write("")

    print("\nФайловий логгер (логи записуються у файл log.txt):")
    file_logger = FileLogger(log_file)
    file_logger.Log("Це звичайне повідомлення")
    file_logger.Error("Це повідомлення про помилку")
    file_logger.Warn("Це попереджувальне повідомлення")

    print("\nВміст файлу log.txt:")
    with open(log_file, "r", encoding="utf-8") as f:
        print(f.read())


if __name__ == "__main__":
    main()
