class Account:
    def __init__(self,name,password):
        self.name = name
        self.__password = password # __ before the variable name turns it into local variable and won't be accessable globally 
        
    def reset_password(self):
        print(self.__password)
        
    def __hello(): # private method 
        print("hello")
        
        
        
acc1 = Account("Sibgatullah",12345)

print(acc1.name)
print(acc1.reset_password()) # accissing the private value with a mathod 
# print(acc1.__password) # can't access private value with public methods

class Person:
    __name = "Person"
    
    def __hello(self):
        print("Hello Person")
        
    def welcome(self):
        self.__hello()
        
p1 = Person()

print(p1.welcome())