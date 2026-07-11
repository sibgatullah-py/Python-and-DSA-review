# When one class(child/derived) derives the properties & methods of another class(parent/base).

class Car:
    @staticmethod
    def start(name):
        print(f"{name} started")
        
    # This is a decorator used to define a method inside a class that does not access or modify class-specific or instance-specific data
    @staticmethod 
    def stop(name):
        print(f"{name} stopped")
        
class Toyota(Car): # Single Inheritance 
    def __init__(self,brand):
        self.brand = brand
        
class Model(Toyota): # Multi-level Inheritance
    def __init__(self,model):
        self.model = model
    
    
car1 = Model("Fortuner")
car2 = Model("Corola")

print(car1.start(car1.model))
print(car2.stop(car2.model))




# Multiple Inheritance
class Father:
    blood = 'A'
    
class Mother:
    blood = 'B'
    
class Child(Father,Mother):
    blood = Father.blood + Mother.blood
    
child1 = Child()

print(child1.blood)