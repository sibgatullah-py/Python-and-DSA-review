def main():
    number= get_number()
    print(f"The number is {number}")


def get_number():
    while True:
        try:
            return int(input("What's the number? "))
        except ValueError:
            print("The number isn't a plain number")

main()
    
"""
What us happening here is that i am saying try executing the first code , if anything goes wrong then catch the error in except and 
flag the error message and else when everything is fine just show the number
"""