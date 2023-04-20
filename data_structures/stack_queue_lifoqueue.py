from queue import LifoQueue

# lClubs = LifoQueue(("ZSC Lions", "SC Bern", "HC Lugano", "EV Zug"))

drinks = LifoQueue(maxsize=3) #LIFO Last In First Out

drinks.put("Coca Cola")
drinks.put("Sprite")
drinks.put("Fanta")

# drinks.put_nowait("Bluna")

print(drinks.get())
print(drinks.get())
print(drinks.get())
# print(drinks.get_nowait())

