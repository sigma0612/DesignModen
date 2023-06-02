from abc import abstractmethod


class TaxStrategy:
    @abstractmethod
    def calculate(self):
        pass


class CN(TaxStrategy):
    def calculate(self):
        return 1


class US(TaxStrategy):
    def calculate(self):
        return 2


class FR(TaxStrategy):
    def calculate(self):
        return 3


class JP(TaxStrategy):
    def calculate(self):
        return 4


class SalesOrder:
    def __init__(self, strategy: TaxStrategy):
        self.strategy = strategy

    def calculate_tax(self):
        return self.strategy.calculate()