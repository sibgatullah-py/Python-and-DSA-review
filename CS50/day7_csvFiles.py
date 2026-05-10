students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",") # Assigning 2 variables side by side 
        student = {"name":name,"house":house}
        students.append(student)


def get_name(student): # the lambda function billow is actually doing the same thing as this func
    return student['name']
    
for student in sorted(students, key= lambda student: student['name']): # lambda parameter: return value 
    print(f"{student['name']} is in {student['house']}")