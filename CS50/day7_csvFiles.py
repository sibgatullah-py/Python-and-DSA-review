students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",") # Assigning 2 veriables side by side 
        student = {"name":name,"house":house}
        students.append(student)


def get_name(student):
    return student['name']
    
for student in sorted(students, key=get_name):
    print(f"{student['name']} is in {student['house']}")