from Lab02.task1.Classes.Subscription import Subscription

class DomesticSubscription(Subscription):
    def __init__(self):
        super().__init__(
            monthly_fee=10.0,
            min_period=1,
            channels=["Новини", "Спорт", "Розваги"],
            features=["HD"]
        )

    def subscription_type(self) -> str:
        return "Domestic"