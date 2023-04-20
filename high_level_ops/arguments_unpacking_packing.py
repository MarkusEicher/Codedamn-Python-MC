contacts = {
    'Alice': '703-493-1834', 
    'Bob': '857-384-1234',
}


def add_contact(name, phone_number):
    contacts[name.capitalize()] = phone_number

# dale = ('dale', '857-384-1234') # tuple
dale = {'name': 'dale', 'phone_number': '857-384-1234'}

# add_contact(*dale) # unpacking tuple
add_contact(**dale) # unpacking dict

print(contacts)

lst = [0, 0, 1]
dt = {"val": 0, "num": 0}

def test(*arg, **kwargs): # packing operator * **
    print(arg, kwargs)

test(*lst, **dt) # unpacking operator * **

name = 27
age = "John"

print(name, age)
# use tuple unpacking
name, age = age, name
print(type(name), age)
