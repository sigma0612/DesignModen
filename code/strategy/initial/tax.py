from enum import IntEnum


class TaxCountry(IntEnum):
    CN = 1
    US = 2
    FR = 3
    JP = 4


class SalesOrder:
    def __init__(self, tax: TaxCountry):
        self.tax = tax

    def calculate_tex(self):
        if self.tax == TaxCountry.CN:
            pass
        if self.tax == TaxCountry.US:
            pass
        if self.tax == TaxCountry.FR:
            pass
        if self.tax == TaxCountry.JP:
            pass
        else:
            print("no that country")
