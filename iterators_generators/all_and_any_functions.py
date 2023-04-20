lst = []

while True:

    match input("Add more items? (y/n): "):

        case "y":
            item = input("Item: ")
            lst.append(item)
        
        case "n":
            break

# print(lst)



if any(lst):
    print("Some good values")
else:
    print("useless input.")

# if any(lst):
#     print("Some good values")
# else:
#     print("useless input.")

print(lst)