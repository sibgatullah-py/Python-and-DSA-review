fruit = input('Your fruit name: ')
color = input("What is the color of your fruit? ")

if color == 'green':
    print(f'{fruit} unripe')
elif color == 'yellow':
    print(f'{fruit} ripe')
elif color == 'brown':
    print(f'{fruit} overripe')
else:
    print('Invalid Color')