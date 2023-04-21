# visitor = {
#     "name": input ("Name: "),
#     "age": int(input ("Age: "))
# }

friends = ["Markus", "Christoph"]

# match visitor:

#     case {"name": "Mike"}:
#         print("Hello Mike")

#     case {"name": name,} if name in friends:
#         print(f"Hey Dude!")
    

from collections import namedtuple

Person = namedtuple("Person", ("name", "age"))

visitor = Person(name = input("Name: "), age = int(input("Age: ")))

match visitor:

    # case Person(name = name) if name in friends:
    case Person(name = "Mike"):
        print("Hey Friend!")
    
    case Person(name = "Sam", age = 28):
        print(f"Hey {visitor.name}, your room number is 50!")