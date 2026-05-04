def main():
    num = int(input("What is the number? "))
    print(f"Square of {num} is",square(num))
    
def square(num):
    return num*num

if __name__ == "__main__":
    main()