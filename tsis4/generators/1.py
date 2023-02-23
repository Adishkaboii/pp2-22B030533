def generate_squares():
    n = int(input("Enter the number: "))
    i = 1
    while i <= n:
        yield i**2
        i += 1
        
for square in generate_squares():
    print(square)
