Create a List:

thislist = ["apple", "banana", "cherry"]
print(thislist)

Print the number of items in the list:

thislist = ["apple", "banana", "cherry"]
print(len(thislist))

What is the data type of a list?

mylist = ["apple", "banana", "cherry"]
print(type(mylist))

Using the list() constructor to make a List:

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

Print the second item of the list:

thislist = ["apple", "banana", "cherry"]
print(thislist[1])

Print the last item of the list:

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

Return the third, fourth, and fifth item:

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

This example returns the items from "orange" (-4) to, but NOT including "mango" (-1):

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

Check if "apple" is present in the list:

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
  
  Change the second item:

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

Insert "watermelon" as the third item:

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)
