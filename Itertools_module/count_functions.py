from itertools import count

counter = count() # Takes start and step arguments

lst = ["Milk", "Honey", "Bread", "Butter"]
# print(next(counter))
# print(next(counter))
# print(next(counter))

# for num in counter:
#     print(num)

#     if num == 10:
#         break

for index, item in zip(counter, lst):
    print(index, item, sep=". ")
