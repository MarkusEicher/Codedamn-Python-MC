from dataclasses import dataclass
from store.cart import Cart, SortOptions
from store.product import Product

# class User:

#     def __init__(self, fname, lname):
#         self.firs_name = fname
#         self.last_name = lname


# with dataclass import this is the same as above:
@dataclass
class User:
    first_name: str
    last_name: str

john = User("John", "Doe")

print(john.first_name)
print(john.last_name)

# Classes that are not used to create objects are called enums

cart = Cart()
cart.add_product(Product("Cup", 10))
cart.add_product(Product("Book", 20))
cart.add_product(Product("Clock", 30))

cart.sort_products(attr=SortOptions.title)
cart.show_product()