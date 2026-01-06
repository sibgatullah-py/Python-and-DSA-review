import time 

def timer(func):
    def wrapper(*args,**kwargs): # *args means this function can take unlimited arguments 
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {end-start} time")
        return result
    return wrapper

@timer # using the function as decorator 
def example_function(n):
    time.sleep(n)
    
example_function(5)

'''
The syntax to create a decorator function is to make a nested function as shown here . It's the required syntax of custom decorators
'''