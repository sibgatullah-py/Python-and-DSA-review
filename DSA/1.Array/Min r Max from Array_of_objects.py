import csv

print("Put 0 if you want to read the file . Put 1 if you want to write in the file")
rotation = int(input())

class Student:
    def __init__(self, name, roll, mark):
        self.name = name
        self.roll = roll
        self.mark = mark
            
if rotation == 1:

    students = []

    number = int(input("How many students: "))
    for s in range(number):
        name = input("Name: ")
        roll = int(input("Roll: "))
        mark = int(input("Mark: "))
        
        students.append(Student(name, roll, mark))
        
    students = sorted(students, key=lambda s: s.roll)
        
    with open('students.csv', 'a', newline='') as file:
        write = csv.DictWriter(file, fieldnames=['name','roll','mark'])
        for s in students:
            write.writerow({
                'name': s.name,
                'roll': s.roll,
                'mark': s.mark
            })
        
        
elif rotation == 0:
    info = []
    with open('students.csv') as file:
        reader = csv.DictReader(file)
        for row in reader:
            info.append({"name":row['name'], "roll":row['roll'], "mark":row['mark']})
            
    for student in info:
        print(student['name'], student['roll'], student['mark'])
        
    total = len(info)
      
    if total > 1:
        mn = min(info, key= lambda x: x['mark'])
        mx = max(info, key= lambda x: x['mark'])
        print(f"Lowest: {mn['name']}, {mn['roll']}, {mn['mark']}")
        print(f"Highest: {mx['name']}, {mx['roll']}, {mx['mark']}")
    elif total == 1:
        print(f"Highest: {info[0]['name']}, {info[0]['roll']}, {info[0]['mark']}")
    else:
        print("No student data found..")
        
else:
    assert False, "Please enter number between 1 or 0. INVALID INPUT!!"