from store.currency import Currency, Dollar, Euro

bill = Dollar(100)
bigbill = Dollar(1000)

bill.change_symbol("£")
bill.show()
bigbill.show()

d = Dollar(12)
e = Euro.from_dollar(d)
e.show()

# Using type to create a class
name = "Francs"
bases = (Currency, )
body = {
    "symbol:": "S",
    "__add__": lambda self, y: self.value + y.value,    
}

Francs = type(name, bases, body)

bill = Francs(100)
print(bill)
print(bill.symbol)