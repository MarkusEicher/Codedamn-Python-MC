num = 0 # global variable
globals()['num2'] = 2 # alternative way to define a global variable


def change(x):
    x = 2   # local variable
    num = 1 # local variable 
    print(num) # This returns 1
    print(locals()) # Returns a dictionary of all local variables

change(0)

# print(x) # x is undefined becaus not accessible outside the function
print(num) # This returns 0

# print(num2) # This returns 2 - Linting gives a warning, but num2 is defined as a global variable
print((globals())) # Returns a dictionary of all global variables