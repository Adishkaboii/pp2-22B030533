def squares():
    a = int(input("Enter 1st bound: "))
    b = int(input("Enter 2nd bound: "))
    for i in range(a, b+1):
        yield i**2
        i+= 1
        
for square in squares():
    print(square)
