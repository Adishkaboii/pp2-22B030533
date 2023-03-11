import re

str = input()

def snake_to_camel(snake):
        return ''.join(x.capitalize() for x in snake.split('_'))

print(snake_to_camel(str))
