class Temperature:
        
    @staticmethod
    def celsius_to_fahrenheit(temp):
        f = (temp * (9/5))+32
        print(f"Temperature is {f} fahrenheit")
    
    @staticmethod    
    def fahrenheit_to_celsius(temp):
        c = (temp-32)*(5/9)
        print(f"Temperature is {c} celsius")
        
temp1 = Temperature.fahrenheit_to_celsius(45)