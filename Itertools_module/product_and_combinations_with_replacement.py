from itertools import product, combinations_with_replacement

team_a = ["John", "Dale", "Harry"]
team_b = ["Linda", "Mary", "Sarah"]

color = ["blue", "red", "green", "yellow"]

for pair in product(team_a, team_b):
    print(pair)


for mix in combinations_with_replacement(color, 2): # Combines from left to right skipping most left after iteration
    print(mix)