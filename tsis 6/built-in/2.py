import math 

u = 0 
l = 0
string = input()

for i in string:
    if i == i.lower():
        l += 1
    else:
        u += 1

print("Uppers: ", u,"Lowers: ", l)
