import uuid

from user import *

class Product:
    def __init__(self,name,price,stock):
        self.id = str(uuid.uuid1())
        self.name = name
        self.price = price
        self.stock = stock
        
    def __str__(self):
        return f"Product ID: {self.id}\nProduct Name: {self.name}\nProduct Price: {self.price}\nAvailable Products: {self.stock}\n"
        
        
        
class Store:
    def __init__(self):
        self.products = []
        
        
    def add_product(self):
        name = input("Product name: ")
        price = int(input("Product price: "))
        stock = int(input("Product stock: "))
        product = Product(name,price,stock)
        self.products.append(product)
        
    def edit_product(self,product_id):
        for product in  self.products:
            if product_id == product.id:
                name = input("Product name: ")
                price = int(input("New price: "))
                stock = int(input("New stock: "))
                
                product.name = name
                product.price = price
                product.stock += stock
                return
    
    def delete_product(self,product_id):
        for index,product in enumerate(self.products):
            if product_id == product.id:
                self.products.pop(index)
                print(f"ID {product_id} is removed")
                return
    
    def view_product(self):
        for product in self.products:
            print(product)
    
    def search_product(self,product_id):
        for product in self.products:
            if product_id == product.id:
                print(product)
                return
        