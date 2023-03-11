import re

text = input()
pattern = r'a.b$'
r = re.findall(pattern, text)
print(r)
