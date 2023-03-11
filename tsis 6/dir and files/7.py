import os

source = 'row.txt'
destination = 'mylist.txt'

with open(source, 'r') as s, open(destination, 'w') as d:
    for line in s:
        d.write(line)
