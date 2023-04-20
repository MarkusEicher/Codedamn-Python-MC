from itertools import combinations, permutations

players = ["John", "Kyle", "Dale", "Billy"]

for group in combinations(players, 2): # Gives back all combinations of the players list
    print(group)

for seats in permutations(players, 2): #Gives all combos with respect to the positions of the players
    print(seats)

import itertools

# Compute the cartesian product of two iterables
product = list(itertools.product([1, 2], ['a', 'b']))
print(product) # Output: [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')]

# Compute all permutations of the elements in an iterable
permutations = list(itertools.permutations([1, 2, 3]))
print(permutations) # Output: [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
