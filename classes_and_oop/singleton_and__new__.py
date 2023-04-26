from store.cart import Cart
from store.product import Product

cart = Cart()

cart.add_product(Product("Phone", 100))
cart.add_product(Product("Laptop", 1000))

cart2 = Cart()
cart2.show_product()

cart.add_product(Product("Clock", 50))
cart3 = Cart()
cart3.show_product()


