from collections import defaultdict

d = defaultdict(int)
d['a'] = 3.14165
# without defaultdict this will through a key error
print(d['b'])