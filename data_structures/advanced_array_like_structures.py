# empty arrays
lst = []
tpl = ()
dct = {}
set = set()

print(type(lst), type(tpl), type(dct), type(set))

# arrays with only one element

lst = [1]
tpl = (1,) # without the trailing comma, it is interpreted as an int only
dct = {1:1}
set = {1}

print(lst, tpl, dct, set)
print(type(lst), type(tpl), type(dct), type(set))
print(len(lst), len(tpl), len(dct), len(set))

row = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(row[0:8:2])
print(row[1:8:2])
print(row[::2])
print(row[::-1])
