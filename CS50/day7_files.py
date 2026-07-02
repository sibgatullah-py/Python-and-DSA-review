name = input("What's your name? ")
if name == "none":
    pass
elif name:
    with open('name.txt','a') as file:
        file.write(f"{name}\n") 
    

names = []    

with open('name.txt','r') as file:
    for line in file:
        names.append(line.rstrip())
    
for each in sorted(names):
    print(each)
    
    
    

    