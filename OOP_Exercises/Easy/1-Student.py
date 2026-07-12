class Student:
    def __init__(self,name,age,department):
        self.name = name
        self.age = age
        self.department = department
        
    def introduce(self):
        print(f"Name: {self.name}, Age: {self.age}, Department: {self.department}")
        
s1 = Student('Ayato',25,'Hydro')
s2 = Student('Diluc',28, 'Pyro')
s3 = Student('Skirk',300, 'Cryo')

s1.introduce()
s2.introduce()
s3.introduce()