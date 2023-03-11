import re

text = input()
pattern = r'[a-z]+(?:_[a-z]+)+'
r = re.findall(pattern, text)
print(r)
