dale = dict(name="Dale" , age=35)

dale["age"] = 40
# dale.age = 40 # This will not work because we can't use the dot notation here

from types import SimpleNamespace

john = SimpleNamespace(name="John" , age=35)
john.age = 40 # This will work because we can use the dot notation here as well because it's a SimpleNamespace

john.height = 1.75 # Assigning new values to a SimpleNamespace object

print(john.name)    
print(john.age)

from collections import namedtuple

Person = namedtuple("Person" , ("name" , "age"))

john = Person("John", 35)
dale = Person("Dale", 40)

print(john)
print(type(dale))