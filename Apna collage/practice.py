# with open('new.txt', "w+") as f:
#     f.write("This is a demo text. Hello!!")
#     data = f.read()
#     print(data)

f = open('new.txt','r+')
f.write("Unga Bunga ")
f.seek(1)
data = f.read()
print(data)
f.close()