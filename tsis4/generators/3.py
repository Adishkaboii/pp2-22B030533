def generate_numbers():
    n = int(input("Enter the number: "))
    i = 1
    for i in range (n+1):
        if i % 3 == 0 and i % 4 == 0:
          print(i)
        
for good in generate_numbers():
    print(good)
