from itertools import accumulate, groupby
from operator import add, sub, mul

age = [12, 22, 32, 42, 52]

for acc_age in accumulate(age, add ): # Accumulates the values by adding, subtract and multiply alternatively
    print(acc_age)

people = [
    {'name': 'Jake', 'adult': True},
    {'name': 'John', 'adult': True},
    {'name': 'Alice', 'adult': True},
    {'name': 'Bob', 'adult': False},
    {'name': 'Darren', 'adult': False}
]


adult_select = lambda person: person['adult']

for group in groupby(people, adult_select):
    print("Adult" if group[0] else "Minor")

    print([person['name']
           for person in group[1]])

