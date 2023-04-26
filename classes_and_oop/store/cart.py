from store.product import Product, EBook
from enum import Enum

class SortOptions(Enum):
    price = "price"
    title = "title"


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
        # print("_init called")
        self._products: list[Product] = [] 

    # def __init__(self):
    #     print("init called")
    #     self._products = []

    def add_product(self, product):
        self._products.append(product)

    
    @property
    def total_products(self):
        return len(self._products)
    
    def total_price(self):
        total = 0
        for product in self._products:
            total += product.price
        return total
    
    def sort_products(self, attr=SortOptions.price):
        self._products.sort(
            # key=lambda product: product.price
            key=lambda product: getattr(
                product, attr.value
            )
        )

    def show_product(self):
        for product in self._products:
            print(product.title, product.price)
        print(f"{'Total Products'}{self.total_products:>2}{'Total Price:':>15}{self.total_price():>5}")

    
    def __iter__(self):
        self._counter= 0
        return(self)
    
    def __next__(self):
        if self._counter < self.total_products:
            ele = self._products[self._counter]
            self._counter +=1 
            return ele
        elif self._counter >= self.total_products:
            raise StopIteration
