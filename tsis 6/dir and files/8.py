import os

Path = input()

if os.path.exists(Path):
    os.remove(Path)
else:
    print("File doesn't exists")
