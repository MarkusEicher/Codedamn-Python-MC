from store.product import Product, EBook
from store.cart import Cart

# from classes_inheritance import Product, EBook, Cart


cart = Cart()

cart.add_product(Product('Honey', 3.50))
cart.add_product(Product('Bread', 2))
cart.add_product(EBook("Book1", 25, 180))
cart.add_product(Product('Milk', 3))
cart.add_product(EBook("Book2", 33, 430))

cart.sort_products()

# print(cart.total_price())
# print(cart.total_products())
cart.show_product()

