import re

text = input()
pattern = r'[A-Z]+[a-z]+'
r = re.findall(pattern, text)
print(r)
