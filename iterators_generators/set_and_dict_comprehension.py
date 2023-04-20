# List comprehension
lst = [ x
       for x in range(3) ]
print(lst)

# Set comprehension
set1 = { y
        for y in range(3)}
print(set1)

# Dict comprehension
dict1 = { z: z*2
         for z in range(10)}
print(dict1)

# An inner and outer loop
for x in range(3):
    for y in range(3):
        print(x, y)

# This inner and outer loop in list comprehension
lst1 = [ f"{x}{y}"
        for x in range(3)
        for y in range(3)]
print(lst1)