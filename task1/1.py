from abc import ABC, abstractmethod

# Абстрактні класи девайсів
class Laptop(ABC):
    @abstractmethod
    def info(self) -> str:
        pass

class Netbook(ABC):
    @abstractmethod
    def info(self) -> str:
        pass

class EBook(ABC):
    @abstractmethod
    def info(self) -> str:
        pass

class Smartphone(ABC):
    @abstractmethod
    def info(self) -> str:
        pass

# Конкретні девайси бренду IProne
class IProneLaptop(Laptop):
    def info(self) -> str:
        return "IProne Laptop - MacBook Air"

class IProneNetbook(Netbook):
    def info(self) -> str:
        return "IProne Netbook - iNet mini"

class IProneEBook(EBook):
    def info(self) -> str:
        return "IProne EBook - iRead"

class IProneSmartphone(Smartphone):
    def info(self) -> str:
        return "IProne Smartphone - iPhone Pro Max"

# Конкретні девайси бренду Kiaomi
class KiaomiLaptop(Laptop):
    def info(self) -> str:
        return "Kiaomi Laptop - Mi Notebook"

class KiaomiNetbook(Netbook):
    def info(self) -> str:
        return "Kiaomi Netbook - Mi Netbook Lite"

class KiaomiEBook(EBook):
    def info(self) -> str:
        return "Kiaomi EBook - Mi Reader"

class KiaomiSmartphone(Smartphone):
    def info(self) -> str:
        return "Kiaomi Smartphone - Redmi Note"

# Конкретні девайси бренду Balaxy
class BalaxyLaptop(Laptop):
    def info(self) -> str:
        return "Balaxy Laptop - Galaxy Book"

class BalaxyNetbook(Netbook):
    def info(self) -> str:
        return "Balaxy Netbook - Galaxy Net Lite"

class BalaxyEBook(EBook):
    def info(self) -> str:
        return "Balaxy EBook - Galaxy EReader"

class BalaxySmartphone(Smartphone):
    def info(self) -> str:
        return "Balaxy Smartphone - Galaxy S Ultra"

# Абстрактна фабрика
class TechFactory(ABC):
    @abstractmethod
    def create_laptop(self) -> Laptop:
        pass

    @abstractmethod
    def create_netbook(self) -> Netbook:
        pass

    @abstractmethod
    def create_ebook(self) -> EBook:
        pass

    @abstractmethod
    def create_smartphone(self) -> Smartphone:
        pass

# Конкретні фабрики брендів
class IProneFactory(TechFactory):
    def create_laptop(self) -> Laptop:
        return IProneLaptop()

    def create_netbook(self) -> Netbook:
        return IProneNetbook()

    def create_ebook(self) -> EBook:
        return IProneEBook()

    def create_smartphone(self) -> Smartphone:
        return IProneSmartphone()

class KiaomiFactory(TechFactory):
    def create_laptop(self) -> Laptop:
        return KiaomiLaptop()

    def create_netbook(self) -> Netbook:
        return KiaomiNetbook()

    def create_ebook(self) -> EBook:
        return KiaomiEBook()

    def create_smartphone(self) -> Smartphone:
        return KiaomiSmartphone()

class BalaxyFactory(TechFactory):
    def create_laptop(self) -> Laptop:
        return BalaxyLaptop()

    def create_netbook(self) -> Netbook:
        return BalaxyNetbook()

    def create_ebook(self) -> EBook:
        return BalaxyEBook()

    def create_smartphone(self) -> Smartphone:
        return BalaxySmartphone()

# Демонстрація роботи програми
def main():
    # Створюємо фабрики
    iprone_factory = IProneFactory()
    kiaomi_factory = KiaomiFactory()
    balaxy_factory = BalaxyFactory()

    # Створення девайсів бренду IProne
    print("=== IProne Products ===")
    print(iprone_factory.create_laptop().info())
    print(iprone_factory.create_netbook().info())
    print(iprone_factory.create_ebook().info())
    print(iprone_factory.create_smartphone().info())

    # Створення девайсів бренду Kiaomi
    print("\n=== Kiaomi Products ===")
    print(kiaomi_factory.create_laptop().info())
    print(kiaomi_factory.create_netbook().info())
    print(kiaomi_factory.create_ebook().info())
    print(kiaomi_factory.create_smartphone().info())

    # Створення девайсів бренду Balaxy
    print("\n=== Balaxy Products ===")
    print(balaxy_factory.create_laptop().info())
    print(balaxy_factory.create_netbook().info())
    print(balaxy_factory.create_ebook().info())
    print(balaxy_factory.create_smartphone().info())

if __name__ == "__main__":
    main()
