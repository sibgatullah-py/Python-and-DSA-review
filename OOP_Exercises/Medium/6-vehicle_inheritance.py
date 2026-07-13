class Vehicle:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
        
class Car(Vehicle):
    def __init__(self,brand,model,color,fuel):
        super().__init__(brand,model)
        self.color = color
        self.fuel = fuel
        
    def display_info(self):
        print(f"Brand: {self.brand},\n" 
              f"Model: {self.model},\n" 
              f"Color: {self.color},\n"
              f"Fuel type: {self.fuel}"
              )
        
car1 = Car('toyota','corola','white','patrol')
car1.display_info()