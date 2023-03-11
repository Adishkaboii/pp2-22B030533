import os 

mylist = ["addition", "from", "mylist", "777"]
file = "mylist.txt"

with open(file, "w") as file:
    for i in mylist:
        file.write("%s\n" % i)

print(file)
