import csv

class Student:
    def __init__(self, name, roll, mark):
        self.name = name
        self.roll = roll
        self.mark = mark
        

students = []

number = int(input("How many students: "))
for s in range(number):
    name = input("Name: ")
    roll = int(input("Roll: "))
    mark = int(input("Mark: "))
    
    students.append(Student(name, roll, mark))
    
students = sorted(students, key=lambda s: s.mark, reverse=True)
    
with open('students.csv', 'a', newline='') as file:
    write = csv.DictWriter(file, fieldnames=['name','roll','mark'])
    write.writerow({'name':name,'roll':roll,'mark':mark})
    for s in students:
        write.writerow({'name':s.name,'roll':s.roll,'mark':s.mark})