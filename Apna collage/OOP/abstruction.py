class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False
        
    def start(self):
        self.clutch = True
        self.acc = False
        print("Car started to move..")
        
    def stop(self):
        self.brk = True
        self.acc = False
        print("Car stopped...")
        
        
car1 = Car() # Object created

car1.start()
car1.stop()
# While the methods are called the self.clutch and others are working in background and not shown to user. This is abstraction(hidden).
