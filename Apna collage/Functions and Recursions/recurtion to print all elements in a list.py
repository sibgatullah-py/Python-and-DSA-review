def print_list(list, idx):
    if idx == len(list):
        return 
    print(list[idx])
    print_list(list,idx+1)
    
    
a = [1,2,3,4,5,6,7]
print(print_list(a,0))