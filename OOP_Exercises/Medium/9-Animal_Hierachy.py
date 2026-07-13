class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def sound(self) -> str:
        return "makes sound"
        
class Mammal(Animal):
    def __init__(self,name,age,group):
        super().__init__(name,age)
        self.group = group
        
    def has_fur(self,has_fur) -> str:
        if has_fur == True:
            self.fur = True
        return f"{self.name} Has Fur"
    
    def info(self,name) -> str:
        return f"{name} is a mammal creature which drinks mother's milk"
    
class Dog(Mammal,Animal):
    def __init__(self,name,age,group,breed):
        super().__init__(name,age,group)
        self.breed = breed
        
    def sound(self) -> str:
        return f"{self.name} sounds Woof Woof!"
    
    def info(self) -> str:
        message = super().info(self.name)
        print(message)
    
class Cat(Mammal,Animal):
    def __init__(self,name,age,group,breed):
        super().__init__(name,age,group)
        self.breed = breed
        
    def sound(self) -> str:
        return f" {self.name} sounds Meow Meow!"
    
    def info(self) -> str:
        message = super().info(self.name)
        print(message)
  
  
# sound() info() has_fur()      

dog = Dog("Max",5,"Mammal","shepard")
print(dog.has_fur(True))
print(dog.sound())
dog.info()