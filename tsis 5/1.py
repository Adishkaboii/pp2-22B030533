import re

s = input()
r = re.findall(r"ab*", s)
print(r)
