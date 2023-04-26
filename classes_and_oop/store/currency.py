class Currency:
    symbol = ""

    def __init__(self, val):
        self.value = val

    def show(self):
        print(f"{self.symbol}{self.value}")

    # Overloading the operator here
    def __add__(self, currency):
        return self.value + currency.value
    
    def __int__(self):
        return int(self.value)

    def __repr__(self):
        return f"{self.symbol}{self.value}"



class Dollar(Currency):
    symbol = "$"

    @classmethod
    def change_symbol(cls, symbol):
        cls.symbol = symbol


class Euro(Currency):
    symbol = "€"

    @staticmethod
    def from_dollar(dollar: Dollar):
        return Euro(dollar.value * 0.89)