class Product:
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def apply_discount(self, percent):
        # self.price = self.price * (1 - percent / 100)
        # print(self.price)
        discount = self.price * percent/100
        self.price -= discount

class EBook(Product):
    def __init__(self, title, price, pages):
        super().__init__(title, price)
        self.pages = pages