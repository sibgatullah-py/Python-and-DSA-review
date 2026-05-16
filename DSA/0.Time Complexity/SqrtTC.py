import math
n = int(input())
li = []

for i in range(1,int(math.sqrt(n))+1):# sqrt() returns float so you need to type cast 
    if n%i == 0: # logic for divisor 
        li.append(i)
        li.append(int(n/i))
li = list(set(li))
li.sort()

for i in li:
    print(i,end=' ')
    
print()
    
# This code only moves to the root of the number so it's complexity is O(sqrt(n))