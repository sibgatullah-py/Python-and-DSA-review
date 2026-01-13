age = int(input("Input the age: "))

if 0 < age < 13:
    print('Child')
elif  age < 20:
    print('Teenager')
elif age < 60:
    print('adult')
elif age >= 60:
    print('Senior')
else:
    print('Wrong Input')