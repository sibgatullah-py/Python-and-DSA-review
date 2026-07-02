def factorial(n):
    fac = 1
    for i in range(1,n+1):
        fac *= i
    
    return fac

a = factorial(4)
print(a)