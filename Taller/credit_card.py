from benefit import Benefit

class CreditCard(Benefit):
    def __init__(self, name, rewards, annual_fee):
        super().__init__(name, rewards)
        self.annual_fee = annual_fee
