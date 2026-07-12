class Circle:
    def __init__(self,radius):
        self.radius = radius
        self.pi = 3.14159
        
    def area(self):
        rad = self.pi*(self.radius**2)
        print(f"Area of the circle is {rad}")
        
    def circumference(self):
        cir = 2*self.pi*self.radius
        print(f"circumference of the circle is {cir}")
        
c1 = Circle(15)
c1.area()
c1.circumference()