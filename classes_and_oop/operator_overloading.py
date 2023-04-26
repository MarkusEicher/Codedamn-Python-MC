class Currency:
    symbol = ""

    def __init__(self, val):
        self.value = val

    def show(self):
        print(f"{self.symbol}{self.value}")

    # Overloading the operator here
    def __add__(self, currency):
        return self.value + currency.value


class Dollar(Currency):
    symbol = "$"

class Euro(Currency):
    symbol = "€"