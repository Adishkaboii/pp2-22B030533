Create a Tuple:

thistuple = ("apple", "banana", "cherry")
print(thistuple)

Print the number of items in the tuple:

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

One item tuple, remember the comma:

thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

String, int and boolean data types:

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

What is the data type of a tuple?

mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

Using the tuple() method to make a tuple:

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

----------------------

Print the second item in the tuple:

thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

Return the third, fourth, and fifth item:

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

--------------

Convert the tuple into a list to be able to change it:

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)
