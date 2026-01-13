age = int(input("Enter customer's age: "))
day = input('Enter which day it is: ')

price = 12 if age >= 18 else 8 if age > 0 else None

if day == 'wednesday':
    price -= 2
    
print(f'ticket price ${price}')