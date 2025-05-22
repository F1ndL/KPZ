from Lab02.task1.Classes.SubscriptionCreator import SubscriptionCreator
from Lab02.task1.Classes.Subscription import Subscription
from Lab02.task1.Classes.DomesticSubscription import DomesticSubscription
from Lab02.task1.Classes.EducationalSubscription import EducationalSubscription
from Lab02.task1.Classes.PremiumSubscription import PremiumSubscription

class ManagerCall(SubscriptionCreator):
    def create_subscription(self, sub_type: str) -> Subscription:
        print("Створення підписки через ManagerCall...")
        sub_type = sub_type.lower()
        if sub_type == "domestic":
            subscription = DomesticSubscription()
        elif sub_type == "educational":
            subscription = EducationalSubscription()
        elif sub_type == "premium":
            subscription = PremiumSubscription()
        else:
            raise ValueError("Невірний тип підписки")

        # Додаємо можливість персонального менеджера до кожної підписки
        subscription.features.append("Персональний менеджер")
        return subscription