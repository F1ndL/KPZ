from Lab02.task1.Classes.SubscriptionCreator import SubscriptionCreator
from Lab02.task1.Classes.Subscription import Subscription
from Lab02.task1.Classes.DomesticSubscription import DomesticSubscription
from Lab02.task1.Classes.EducationalSubscription import EducationalSubscription
from Lab02.task1.Classes.PremiumSubscription import PremiumSubscription

class WebSite(SubscriptionCreator):
    def create_subscription(self, sub_type: str) -> Subscription:
        print("Створення підписки через WebSite...")
        sub_type = sub_type.lower()
        if sub_type == "domestic":
            return DomesticSubscription()
        elif sub_type == "educational":
            return EducationalSubscription()
        elif sub_type == "premium":
            return PremiumSubscription()
        else:
            raise ValueError("Невірний тип підписки")