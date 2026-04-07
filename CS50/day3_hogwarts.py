students = {
    'Harry':'Grffindor',
    'Ron': 'Gryffindor',
    'Malfoy': "Slytherin",
    "Hermione": 'Gryffindor',
}

for student in students:
    print(f"{student} is admitted in {students[student]} house.")
    
    
    
students = [
    {'name':'Hermione', 'house': 'Gryfindor', 'patronus':'Otter'},
    {'name':'Harry', 'house': 'Gryfindor', 'patronus':'Stag'},
    {'name':'Ron', 'house': 'Gryfindor', 'patronus':'Jack Russell terrier'},
    {'name':'Draco', 'house': 'Slytherin', 'patronus':'None'},
]

for student in students:
    print(f"{student['name']} is admitted in {student['house']} with patronus {student['patronus']}")