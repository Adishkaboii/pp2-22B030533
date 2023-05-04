import math

num = int(input())

def f_to_c(num):
    celcius = (5 / 9) * (num - 32)
    return celcius

celcius = f_to_c(num)
print(celcius)
