tpl = ("Dale", 27)

name, age = ("John", 27) # unpacking
name2, age2 = ["Rose", 26] # unpacking
print(name)
print(age, name)
print(name2, age2)

friends = {
    "Ben": "123-456-7890", 
    "Alice": "123-456-7890",
    "Rose": "123-456-7890"
}

contacts = {
    "John": "123-456-7890",
    "Dale": "123-456-7890",
    **friends # unpacking dictionary, for lists it is *
}

# contacts.update(friends)
print(contacts)

# name, age, weight, is_programmer = (
name, *cache, is_programmer = ( 
    ("John", 27, 80, True)
    # ("Alice", 27, 80, False)
    # ("Rose", 27, 80, True)
    # ("Ben", 27, 80, True)
)

print(is_programmer)
print(cache)
print(name)