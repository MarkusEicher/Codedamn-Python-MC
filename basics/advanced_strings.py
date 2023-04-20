path = r"X:\Python\advanced_strings.py" # r means raw string
path2 = "Here I want to print a slash \\"

print (path)
print (path2)
print ("\a") # sound alarm


name  = "John"
age = 25

msg = "Hello, my name is " + name + " and I am " + str(age) + " years old." #string concatenation
print (msg)

msg2 = "Hello, my name is %s and I am %d years old." % (name, age) #string with % notation
print (msg2)

msg3 = f"Hello, my name is {name} and I am {age} years old." #f string notation
print (msg3)

msg4 = "Hello, my name is {} and I am {} years old.".format(name, age) #format dotted string notation
print (msg4)

msg5 = "Hello, my name is {name} and I am {age} years old.".format(age=age, name=name) #format dotted string notation with named arguments
print (msg5)

template_string = "Hello, my name is {name} and I am {age} years old." #format string interpolation with a template
print (template_string.format(name="Bob", age=31))
print (template_string.format(age=30, name="Alice"))
print (template_string.format(name="Dale", age=26))
