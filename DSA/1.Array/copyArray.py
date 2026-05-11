from array import *

val = array('i',[1,2,3,4,5,6,7,8,9])

copyArray = array(val.typecode, (num for num in val))
copyArray.reverse()
for num in copyArray:
    print(num, end=' ')