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

class Cart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def total_products(self):
        return len(self.products)
    
    def total_price(self):
        total = 0
        for product in self.products:
            total += product.price
        return total
    
    def sort_products(self):
        self.products.sort(
            key=lambda product: product.price
        )


milk = Product("Milk", 2)
milk.apply_discount(20)

book = EBook("Book", 30, 200)
book.apply_discount(20)

print(milk.price, book.price)

my_cart = Cart()
my_cart.add_product(Product('Honey', 3.50))
my_cart.add_product(Product('Bread', 2))
my_cart.add_product(EBook("Book", 30, 200))

print(my_cart.total_price())
print(my_cart.total_products())