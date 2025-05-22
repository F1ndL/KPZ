# Zoo Inventory System

## Principles Used

### DRY (Don't Repeat Yourself)
Shared logic for animals is extracted into `Animal` class (see `animal.py:1-5`).

### KISS (Keep It Simple, Stupid)
Each class does only one thing (see `food.py`, `worker.py`).

### SRP (Single Responsibility Principle)
Each class represents a single concept – e.g., `ZooWorker` manages staff only.

### OCP (Open/Closed Principle)
`Animal` може бути розширено новими підвидами без зміни бази (`animal.py`).

### LSP (Liskov Substitution Principle)
Будь-який `Mammal` або `Bird` можна використовувати як `Animal` (див. `main.py`).

### ISP (Interface Segregation Principle)
Кожен клас має простий інтерфейс без зайвих методів.

### DIP (Dependency Inversion Principle)
`ZooInventory` не залежить напряму від реалізацій, а працює з об'єктами.

### Composition Over Inheritance
`ZooInventory` має `animals`, `foods`, `enclosures`, `workers` замість наслідування.

### Fail Fast
`add_animal()` у `Enclosure` викликається явно — краще одразу бачити, що тварина в клітці.

## UML
Дивіться файл `Lab01.png`.