from Lab02.task1.Classes.Subscription import Subscription

class EducationalSubscription(Subscription):
    def __init__(self):
        super().__init__(
            monthly_fee=8.0,
            min_period=3,
            channels=["Документальні", "Освітні", "Дитячі"],
            features=["Субтитри", "Інтерактивні матеріали"]
        )

    def subscription_type(self) -> str:
        return "Educational"