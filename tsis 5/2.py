import re

s = input()
r = re.findall("ab{2,3}", s)
print(r)
