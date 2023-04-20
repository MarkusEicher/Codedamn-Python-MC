lst = [num for num in range(21)] # List comprehension
# for num in range(0, 21):
#     lst.append(num)
print(lst)

names = ["john", "dale", "mike"]
lst2 = [ name.capitalize() for name in names] # List comprehension
print(lst2)


def is_even(num):
    return num%2 == 0

lst3 = [num for num in range(21)
        if is_even(num)]
print(lst3)


lst4 = [num if is_even(num) else "odd"
        for num in range(21)]
print(lst4)