class Student:
    def __init__(self, name,clas,roll):
        self.name = name
        self.clas = clas
        self.roll = roll
        
students = []

n = int(input("number of students"))

for i in range(n):
    name = input('Student name: ')
    clas = int(input("Student class: "))
    roll = int(input("Student roll: "))
    students.append(Student(name,clas,roll))
    
for s in students:
    print(s.name,s.clas,s.roll)