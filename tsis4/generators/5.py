def back():
    a = int(input("Enter upper bound: "))
    while a>=0:
        yield (a)
        a-=1
            
for step in back():
    print(step)
