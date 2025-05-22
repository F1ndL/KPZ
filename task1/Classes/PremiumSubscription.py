from Lab02.task1.Classes.Subscription import Subscription

class PremiumSubscription(Subscription):
    def __init__(self):
        super().__init__(
            monthly_fee=20.0,
            min_period=6,
            channels=["Новини", "Спорт", "Розваги", "Фільми", "Серіали"],
            features=["4K", "Multi-Screen", "Ексклюзивний контент"]
        )

    def subscription_type(self) -> str:
        return "Premium"