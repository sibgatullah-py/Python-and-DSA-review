def main():
    name = input("What's your name? ")
    hello(name)



def hello(name="world"): # world is default parameter value if the user doesn't send any arguments
    print(f"Hello, {name}")
    
    
main()