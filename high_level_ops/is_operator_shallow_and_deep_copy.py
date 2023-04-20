from copy import deepcopy

lst1 = [0,0]
lst2 = [0,0]

lst3 = [0, 0]

lst_copy = lst1 # this creates a pointer

# lst_copy2 = lst3.copy() # shallow copy
lst_copy3 = deepcopy(lst3) # deep copy
# lst_copy2[0] = 1


# print(lst1 == lst_copy)
# print(lst_copy is lst2)
# print(lst_copy is lst1)

print(lst3)