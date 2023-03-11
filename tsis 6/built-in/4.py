import math, time

n = int(input())
t = int(input())
root = math.sqrt(n)

time.sleep(t / 1000)
print(f"Square root of {n} after {t} miliseconds is {root}")
