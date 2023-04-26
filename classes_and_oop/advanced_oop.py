from store.cart import Cart

print(issubclass(Cart, object))

for _ in range(5): # _ is a placeholder for a variable that is not used
    print("🔥")


class Dollar:
    symbol = "$"

    def __init__(self, val):
        self.value = val

bill = Dollar(100)
big_bill = Dollar(1000)

print(bill.value != big_bill.value)