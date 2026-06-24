people = [
    ('alice',25),
    ('bob',18),
    ('jonny',30),
]
byage = sorted(people, key=lambda x:x[1])

print(list(byage))