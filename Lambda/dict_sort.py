employees = [
    {"name": "A", "salary": 5000},
    {"name": "B", "salary": 3000},
    {"name": "C", "salary": 7000}
]

new = sorted(employees, key= lambda x:x['salary'])

print(list(new))