import os, string

for letter in string.ascii_uppercase:
    file = letter + ".txt"
    with open(file, 'w') as f:
        f.write("Hello from file " + letter)
