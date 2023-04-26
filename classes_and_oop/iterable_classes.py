from store.cart import Cart
from store.product import Product

cart = Cart()
cart.add_product(Product("Book", 16.20))
cart.add_product(Product("Wine", 12.20))

for product in cart:
    print(f"{product.title} {product.price}")