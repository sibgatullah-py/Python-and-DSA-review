from array import *

val = array('i',[])

while True:
    num = input("enter the number: ")
    if num == "none":
        break
    else:
        val.append(int(num))
        
for n in val:
    print(n, end=' ')