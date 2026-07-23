from user import *
from store import *

class Cart:
    def __init__(self):
        self.cart = []
        
    def add_product(self):
        pass
    
    def remove_product(self):
        pass
    
    def show_cart(self):
        for product in self.cart:
            print(product.id)
            print(product.name)
            print(product.amount)
            print(product.price)
            print()
    
    def total_price(self):
        pass
    
    def clear_cart(self):
        pass