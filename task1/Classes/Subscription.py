from abc import ABC, abstractmethod

class Subscription(ABC):
    def __init__(self, monthly_fee: float, min_period: int, channels: list, features: list):
        self.monthly_fee = monthly_fee  # Щомісячна плата
        self.min_period = min_period  # Мінімальний період підписки (в місяцях)
        self.channels = channels  # Список каналів
        self.features = features  # Інші можливості

    @abstractmethod
    def subscription_type(self) -> str:
        """Повертає тип підписки"""
        pass

    def __str__(self):
        return (f"{self.subscription_type()} Subscription:\n"
                f"  Щомісячна плата: {self.monthly_fee}\n"
                f"  Мінімальний період: {self.min_period} місяць(ів)\n"
                f"  Канали: {', '.join(self.channels)}\n"
                f"  Можливості: {', '.join(self.features)}\n")
