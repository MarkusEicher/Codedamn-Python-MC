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

    def show_product(self):
        for product in self.products:
            print(product.title, product.price)
        print(f"{'Total Products'}{self.total_products():>2}{'Total Price:':>15}{self.total_price():>5}")