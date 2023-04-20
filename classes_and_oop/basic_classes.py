class Person:
    
    def __init__(self, name, age):
        # print('self:', self)
        self.name = name
        self.age = age

    def show(length):
        
        len_name = len(length.name)
        print(len_name)


objectof = Person('Benjamin', 25)
print(objectof.name, objectof.age)

object2 = Person('Jake', 30)
print(object2.name, object2.age)

objectof._isprogrammer = True
print(objectof._isprogrammer)

# del(objectof._isprogrammer)

objectof.show()


