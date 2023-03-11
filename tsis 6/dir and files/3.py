import os

path = input()

if os.path.exists(path):
    dir, file = os.path.split(path)
    print(f"Directory: {dir}")
    print(f"Filename: {file}")
else:
    print(f"{path} does not exist")
