# Take user's name inout
name = input("What is your name? ")

# Remove space and capitalize
name = name.strip().title()

# Printing user name
print(f"User name is {name}")



x = float(input("What is the first number? "))
y = float(input("what is the second number? "))

z = round(x+y)

print(f"Rounded value is {z:,}")