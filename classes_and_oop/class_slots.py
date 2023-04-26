class User:
    __slots__ = ("first_name", "last_name") # restricts the attributes to be created

    def __init__(self, fname, lname):
        self.first_name = fname
        self.last_name = lname

john = User("John", "Doe")
print(john.first_name)
print(john.last_name)
john.last_name = "Smith"
print(john.last_name)