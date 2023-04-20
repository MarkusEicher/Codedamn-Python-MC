# # User input sample code without walrus operator
# user_input = input("Enter something (or press enter to quit): ")
# while user_input != "":
#     print("You entered:", user_input)
#     user_input = input("Enter something (or press enter to quit): ")


# # Walrus operator sample code makes it easier to read
# while (user_input := input("Enter something (or press enter to quit): ")) != "":
#     print("You entered:", user_input)


friends = {
    'Alice': '703-493-1834',
    'Bob': '857-384-1234',
}
print(friends)

kyle = {"kyle": "857-384-1234"}

contacts = friends | kyle # Pipe joins the two dicts
print(contacts)

erich = {"erich": "857-384-1234"}
# friends.update(erich)
friends |= erich # Pipe also works to update
print(friends)