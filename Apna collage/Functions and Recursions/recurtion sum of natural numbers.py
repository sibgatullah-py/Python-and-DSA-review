def result(n):
    if n == 1:
        return 1
    else:
        return result(n-1)+n
    
print(result(10))