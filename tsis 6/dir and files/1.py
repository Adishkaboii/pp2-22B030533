import os

path = input()

print("Only directories:")

for item in os.listdir(path):
       if os.path.isdir(os.path.join(path, item)):
        print(item)
        
print("\nOnly files:")

for item in os.listdir(path):
       if os.path.isfile(os.path.join(path, item)):
        print(item)
        
print("\nAll directories and files :")
print([ item for item in os.listdir(path)])
