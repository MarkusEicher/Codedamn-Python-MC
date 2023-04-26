from store.cart import Cart
from store.product import Product, EBook

cart = Cart()

cart.add_product(Product("C", 10))
cart.add_product(Product("B", 20))
cart.add_product(Product("A", 30))

cart.sort_products("price")
cart.show_product()

ebook = EBook("Python", 100, 200)
# ebook = EBook("JavaScript", 90, 210)
print(ebook["title"])

ebook["title"] = "C++"
print(ebook["title"])

