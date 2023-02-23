def generate_evens():
    n = int(input("Enter the number: "))
    i = 0
    while i <= n:
        yield i
        i += 2
        
for even in generate_evens():
    print(even)
