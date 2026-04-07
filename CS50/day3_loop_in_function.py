def main():
    n = get_number()
    meow(n)

def get_number():
    while True:
        n = int(input("What's the meow number? "))
        if n > 0:
            return n
        else:
            print("Enter a positive meow number.")

            

def meow(n):
    for _ in range(n):
        print("meow")
        
main()