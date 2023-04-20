from itertools import chain, islice, compress, filterfalse

gen = (x for x in range(2, 12, 2))
lst = [12, 16, 18]
lst1 = [1, 2, 3]

for num in chain(gen, lst, lst1): # Combines the lists or generators together
        print(num)

for num in islice(gen, 0, 2): # Used to slice generators or lists
        print(num)


name = ["Dale", "Jake", "John"]
adult = [True, 0, True]

for adult_name in compress(name, adult): # Select only the values that matches to true
        print(adult_name)

age = [27, 22, 13, 15, 52]

adults = filter(
        lambda age: age >= 18,
        age
)

print ([age for age in adults])