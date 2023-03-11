import re

text = input()
pattern = r'[ ,.]'
r = re.sub(pattern, ':', text)
print(r)
