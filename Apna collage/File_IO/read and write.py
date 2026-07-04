from pathlib import Path

path = Path(__file__).parent / "demo.txt"

with open(path, "r+") as f:
    f.write("This is a demo text. Hello!!")
    # f.seek(0)
    data = f.read()
    print(data)
