list = [1,1,2,3,4,4,3,5,6,7,2,8,9,7]

organized = []

for i in list:
    if i not in organized:
        organized.append(list[i])

print(organized)
