class Parent:
    def __init__(self,name,phone):
        self.pname = name
        self.phone = phone
        
class Student(Parent):
    def __init__(self,pname,phone,sname,roll,cgpa):
        super().__init__(pname,phone)
        self.sname = sname
        self.roll = roll
        self.cgpa = cgpa
        
    def show_info(self):
        print(f"Student: {self.sname}\nRoll: {self.roll}\nCGPA: {self.cgpa}\nParent: {self.pname}\nPhone: {self.phone}")
        
s1 = Student('Alice',123456,'Dyroth',21,3.45)
s1.show_info()