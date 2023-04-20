ht1 = {"Dale": 99002, "Mary": 98002, "John": 98002} # All hashable datatypes can be used as keys

print(hash("John"))
print(hash("Mary"))
print(hash(f"Dale"))

ht2 = dict(Dale=1000, John=1001, Mary=1002) # Declaring a dict with the dict() function

print(hash("John"))
print(hash("Mary"))
print(hash("Dale"))


from types import MappingProxyType

mark = dict(name="Mark", age=25)
proxy = MappingProxyType(mark) # Creating a proxy object read-only

mark["name"] = "John"
print(mark["name"])

# proxy["name"] = "John" # This will raise a TypeError