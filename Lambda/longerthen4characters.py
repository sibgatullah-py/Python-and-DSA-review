words= ['cat','elephant','dog','tiger','chicken']

length = filter(lambda x:len(x)>4,words)
print(list(length))