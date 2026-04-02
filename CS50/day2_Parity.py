def main():
    number = int(input("What's the number? "))
    
    if parity(number):
        print("EVEN")
    else:
        print("ODD")
        
def parity(number):
    return number%2==0

main()