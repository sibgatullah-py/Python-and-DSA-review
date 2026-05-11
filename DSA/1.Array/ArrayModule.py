from array import *

array = array('i',[10,20,30,40,50])

for num in range(0,5):
    print(array[num], end=' ')

print()
    
for num in array: # enhanced for loop 
    print(num, end=' ')
    
print()

print(array.typecode)

print()

array.reverse()

for num in array:
    print(num, end=' ')