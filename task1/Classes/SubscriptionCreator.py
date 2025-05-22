from abc import ABC, abstractmethod
from Lab02.task1.Classes.Subscription import Subscription

class SubscriptionCreator(ABC):
    @abstractmethod
    def create_subscription(self, sub_type: str) -> Subscription:
        pass