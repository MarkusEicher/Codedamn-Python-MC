# Code snippet from the lesson @property decorator for total_products
from store.cart import Cart
from store.product import Product, EBook

cart = Cart()

cart.add_product(EBook("Python", 100, 200))
cart.add_product(EBook("JavaScript", 90, 210))

print(cart.total_products)
print(cart.show_product())

# Code snippet from the lesson property setter and deleter

class User:
    def __init__(self, fname, lname):
        self.first_name = fname
        self.last_name = lname
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    @full_name.setter
    def full_name(self, name: str):
        self.first_name, self.last_name = name.split()

    
print(User("John", "Doe").full_name)