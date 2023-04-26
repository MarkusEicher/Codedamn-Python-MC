class Cart:

    _instance = None

    def __new__(cls):
        # print("new called")
        if cls._instance is None:
            # print("Creating new instance")
            cls._instance = super().__new__(cls)
            # print("Created new instance")
            cls._instance._init()

        return cls._instance
    
    def _init(self):
        print("_init called")
        self._products = []

    # def __init__(self):
    #     print("init called")
    #     self._products = []

    def add_product(self, product):
        self._products.append(product)

    def total_products(self):
        return len(self._products)
    
    def total_price(self):
        total = 0
        for product in self._products:
            total += product.price
        return total
    
    def sort_products(self):
        self._products.sort(
            key=lambda product: product.price
        )

    def show_product(self):
        for product in self._products:
            print(product.title, product.price)
        print(f"{'Total Products'}{self.total_products():>2}{'Total Price:':>15}{self.total_price():>5}")