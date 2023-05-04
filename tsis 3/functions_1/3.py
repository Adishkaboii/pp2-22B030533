def solve(numheads, numlegs):
    for i in range(numheads + 1):
        j = numheads - i
        if (i * 2 + j * 4) == numlegs:
            return (i, j)
    return None

# Test the function with the given numbers
numheads = 35
numlegs = 94
result = solve(numheads, numlegs)
if result is not None:
    i, j = result
    print("Number of chickens:", i)
    print("Number of rabbits:", j)
else:
    print("No solution found")
