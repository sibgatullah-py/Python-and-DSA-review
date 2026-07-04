from pathlib import Path

path = Path(__file__).parent /"../"/ "Functions and Recursions" / "doc.txt"

f = open(path, "r")
out = f.read(100)
print(out)

# line1 = f.readline()
# print(line1)
# line2 = f.readline()
# print(line2)

f.close()