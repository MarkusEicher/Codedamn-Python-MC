lst = ["Milk", "Eggs", "Bread"]

# This is one option to print the formatted list
for index in range(len(lst)):   
    print(f"{index+1}. {lst[index]}")

# The more elegant version using enumerate with the same output
for index, item in enumerate(lst, start=1):
    print(f"{index}. {item}")


# Using the zip() function for formatted output takes the shortest path
name = ["Alice", "Bob", "John", "Jake", "Sarah", "Rose"]
info = [99001, 99002, 99003, 99004, 99005]
for nm, inf in zip(name, info):
    print(nm, inf)

# Using the zip_longest() function for formatted output takes the longest path
from itertools import zip_longest
for nm, inf in zip_longest(name, info, fillvalue=0):
    print(nm, inf)