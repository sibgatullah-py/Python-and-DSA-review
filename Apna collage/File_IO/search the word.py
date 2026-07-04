from pathlib import Path

path = Path(__file__).parent / "example.txt"

with open(path, "r+") as f:
    f.write("Hello guys\n we are learning file i/o \n We are using Python for it.")
    
    f.seek(0)
    
    text = f.read()
    if "i/o" in text:
        print("Found!")
    else:
        print("Not found!")