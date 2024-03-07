# loyalty_program.py
from benefit import Benefit

class LoyaltyProgram(Benefit):
    def __init__(self, name, rewards, membership_fee):
        super().__init__(name, rewards)
        self.membership_fee = membership_fee
