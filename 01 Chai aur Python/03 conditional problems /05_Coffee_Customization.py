size = input('Enter your order size: ')
extra_shot = input('Do you need extra shot? ')

if extra_shot == 'yes':
    coffee = size + ' coffee with extra shot'
else:
    coffee = size + ' coffee'

print(coffee)