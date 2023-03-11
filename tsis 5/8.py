import re

text = input()
pattern = r'[A-Z][^A-Z]*'
r = re.findall(pattern, text)
print(r)
