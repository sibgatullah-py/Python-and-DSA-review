from store import *
from cart import *

class User:
    def __init__(self,name,email,password):
        self.name = name
        self.email = email
        self.password = password


# Admin Methods        
class Admin(User):
    def __init__(self,name,email,password):
        super().__init__(name,email,password)
        self.role = 'admin'
        
    def add_product(self,store,product):
        store.add_product(product)
    
    def edit_product(self,store,product_id):
        store.edit_product(product_id)
    
    def delete_product(self,store,product_id):
        store.delete_product(product_id)
    
    def view_product(self,store):
        store.list_product()
        
    def search_product(self,store,product_id):
        store.search_product(product_id)



# Customer Methods        
class Customer(User):
    def __init__(self, name, email, password):
        super().__init__(name, email, password)
        self.role = 'customer'
        self.cart = Cart() # cart for every customer
        
    def view_cart(self):
        pass
    
    def add_to_cart(self):
        pass
    
    def remove_from_cart(self):
        pass
    
    def checkout(self):
        pass
    
    