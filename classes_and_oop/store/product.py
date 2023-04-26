from abc import ABCMeta, abstractmethod

# abc holds methods to define templates for inherited classes
class BaseProduct(metaclass=ABCMeta):
    
    @abstractmethod
    def __init__(self, title, price) -> None:
        pass
    @abstractmethod
    def apply_discount(self, percent):
        pass



class Product(BaseProduct):
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def apply_discount(self, percent):
        # self.price = self.price * (1 - percent / 100)
        # print(self.price)
        discount = self.price * percent/100
        self.price -= discount

    def __getitem__(self, key):
        return getattr(self, key)
    
    def __setitem__(self, key, value):
        setattr(self, key, value)

class EBook(Product):
    def __init__(self, title, price, pages):
        super().__init__(title, price)
        self.pages = pages

class ElectronicProduct(BaseProduct):
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def apply_discount(self, percent):
        # self.price = self.price * (1 - percent / 100)
        # print(self.price)
        discount = self.price * percent/100
        self.price -= discount

