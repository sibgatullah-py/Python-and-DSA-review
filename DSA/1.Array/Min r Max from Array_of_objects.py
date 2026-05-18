import csv

print("Put 0 if you want to read the file . Put 1 if you want to write in the file")
rotation = int(input())

if rotation == 1:
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
        
        
elif rotation == 0:
    info = []
    with open('students.csv') as file:
        reader = csv.DictReader(file)
        for row in reader:
            info.append({"name":row['name'], "roll":row['roll'], "mark":row['mark']})
            
    for student in info:
        print(student['name'], student['roll'], student['mark'])
        
else:
    assert False, "Please enter number between 1 or 0. INVALID INPUT!!"