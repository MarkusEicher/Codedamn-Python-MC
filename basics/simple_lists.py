""" # Solution of the Masterclass Python 3 Codedamn Course
lst = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# remove elements
lst.remove("cherry")
lst.remove("melon")
lst.remove("kiwi")
# add elements
lst.append("guava")
lst.append("peach")
# reverse the list
lst.reverse()
# print the list
print(lst)
# print the length of the list
print(len(lst)) """

# Better Solution of the Masterclass Python 3 Codedamn Course

lst = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(lst)
lst_to_remove = ["cherry", "kiwi", "melon"]
for item in lst_to_remove:
    if item in lst:
        lst.remove(item)
print(lst)
lst.extend(["guava", "peach"])
print(lst)
lst.reverse()
print(lst)
print(len(lst))