import uuid

class Product:
    def __init__(self,name,price,stock):
        self.id = str(uuid.uuid1())
        self.name = name
        self.price = price
        self.stock = stock
        
    def __str__(self):
        return f"Product ID: {self.id}\nProduct Name: {self.name}\nProduct Price: {self.price}\nAvailable Products: {self.stock}\n"