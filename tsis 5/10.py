import re

def camel_to_snake(camel):
    r = re.findall('[a-zA-Z][^A-Z]*', camel)
    
    snake = '_'.join(w.lower() for w in r)
    
    return snake

camel = input()

snake = camel_to_snake(camel)
print(snake)
