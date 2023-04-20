contacts = {
    'John': '555-1212',
    'Paul': '555-4321',
    'George': '555-2345',
    'Ringo': '555-3456'
}

client = input ("Please enter the name of the client: ")

class CapError(Exception):
    pass

if client[0] != client[0].upper():
    raise CapError(client + " First letter must be uppercase")

try:
    print (client, contacts[client])
except KeyError:
    print(client, "not found")


