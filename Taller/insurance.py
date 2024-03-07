from benefit import Benefit

class Insurance(Benefit):
    def __init__(self, name, coverage, premium):
        super().__init__(name, rewards=None)
        self.coverage = coverage
        self.premium = premium
