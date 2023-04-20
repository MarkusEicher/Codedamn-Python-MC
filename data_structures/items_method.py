contacts = {
    'Alice': '703-493-1834',
    'Bob': '857-384-1234',
    'Elizabeth': '484-584-2923',
    'Eve': '919-123-4567'
}

for name in contacts:
    print(
        name, contacts[name]
    )

for name, info in contacts.items(): # Alternative method with the same result
    print(
        name, info
    )