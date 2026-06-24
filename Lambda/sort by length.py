words = ["banana", 'kiwi', 'apple','mango']

new = sorted(words, key= lambda x:len(x))

print(list(new))