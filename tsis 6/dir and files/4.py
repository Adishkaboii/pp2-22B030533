import os

file = "row.txt"
lines = 0
with open(file, 'r') as f:
    for line in f:
        lines += 1

print("Number of lines in", file, "is:", lines)
