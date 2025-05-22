from abc import ABC, abstractmethod

# --- Абстрактні класи продуктів ---
class Laptop(ABC):
    @abstractmethod
    def create(self):
        pass

class Netbook(ABC):
    @abstractmethod
    def create(self):
        pass

class EBook(ABC):
    @abstractmethod
    def create(self):
        pass

class Smartphone(ABC):
    @abstractmethod
    def create(self):
        pass

# --- Абстрактна фабрика ---
class DeviceFactory(ABC):
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

# --- Конкретні реалізації пристроїв для IProne ---
class IProneLaptop(Laptop):
    def create(self):
        return "Laptop від IProne"

class IProneNetbook(Netbook):
    def create(self):
        return "Netbook від IProne"

class IProneEBook(EBook):
    def create(self):
        return "EBook від IProne"

class IProneSmartphone(Smartphone):
    def create(self):
        return "Smartphone від IProne"

# --- Конкретні реалізації пристроїв для Kiaomi ---
class KiaomiLaptop(Laptop):
    def create(self):
        return "Laptop від Kiaomi"

class KiaomiNetbook(Netbook):
    def create(self):
        return "Netbook від Kiaomi"

class KiaomiEBook(EBook):
    def create(self):
        return "EBook від Kiaomi"

class KiaomiSmartphone(Smartphone):
    def create(self):
        return "Smartphone від Kiaomi"

# --- Конкретні реалізації пристроїв для Balaxy ---
class BalaxyLaptop(Laptop):
    def create(self):
        return "Laptop від Balaxy"

class BalaxyNetbook(Netbook):
    def create(self):
        return "Netbook від Balaxy"

class BalaxyEBook(EBook):
    def create(self):
        return "EBook від Balaxy"

class BalaxySmartphone(Smartphone):
    def create(self):
        return "Smartphone від Balaxy"

# --- Конкретні фабрики ---
class IProneFactory(DeviceFactory):
    def create_laptop(self):
        return IProneLaptop()

    def create_netbook(self):
        return IProneNetbook()

    def create_ebook(self):
        return IProneEBook()

    def create_smartphone(self):
        return IProneSmartphone()

class KiaomiFactory(DeviceFactory):
    def create_laptop(self):
        return KiaomiLaptop()

    def create_netbook(self):
        return KiaomiNetbook()

    def create_ebook(self):
        return KiaomiEBook()

    def create_smartphone(self):
        return KiaomiSmartphone()

class BalaxyFactory(DeviceFactory):
    def create_laptop(self):
        return BalaxyLaptop()

    def create_netbook(self):
        return BalaxyNetbook()

    def create_ebook(self):
        return BalaxyEBook()

    def create_smartphone(self):
        return BalaxySmartphone()

# --- Головна функція ---
def main():
    factories = [IProneFactory(), KiaomiFactory(), BalaxyFactory()]
    for factory in factories:
        laptop = factory.create_laptop()
        netbook = factory.create_netbook()
        ebook = factory.create_ebook()
        smartphone = factory.create_smartphone()

        print(laptop.create())
        print(netbook.create())
        print(ebook.create())
        print(smartphone.create())
        print('-' * 30)

if __name__ == "__main__":
    main()
