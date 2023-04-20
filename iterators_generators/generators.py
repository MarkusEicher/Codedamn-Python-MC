gen = ( x for x in range (4)) # A generator does not assign the values, it just keeps track of the state of them

# print(gen)

for num in gen:
    print(num)


def range_even(end):
    for num in range(0, end, 2):
        # return num # This return ends the execution
        print(f"yielding value {num}")
        yield num 
   
gen = range_even(10)

next(gen)
next(gen)

passwords = ["not good", "give'm_pass", "00100=100"]

def lengths(itr):
    for ele in itr:
        yield len(ele)

def hide(itr):
    for ele in itr:
        yield ele * "*"

for password in hide(lengths(passwords)):
    print(password)