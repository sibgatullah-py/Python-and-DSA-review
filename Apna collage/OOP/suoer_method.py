class Car:
    def __init__(self,type):
        self.type = type
    
    @staticmethod
    def start(name):
        print(f"{name} started")
        
    # This is a decorator used to define a method inside a class that does not access or modify class-specific or instance-specific data
    @staticmethod 
    def stop(name):
        print(f"{name} stopped")
        
class Toyota(Car): # Single Inheritance 
    def __init__(self,brand,type):
        self.brand = brand
        
        super().__init__(type) # super() method allows us to access parent class's methods 
        

car1 = Toyota("Toyota","dessel")

print(car1.type)