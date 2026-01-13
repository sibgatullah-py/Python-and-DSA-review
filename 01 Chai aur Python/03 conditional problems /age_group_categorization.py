age = int(input("Input the age: "))

if 0 < age < 13:
    print('Child')
elif 13 <= age <= 19:
    print('Teenager')
elif 20<=age<=59:
    print('adult')
elif age >=60:
    print('Senior')
else:
    print('Wrong Input')