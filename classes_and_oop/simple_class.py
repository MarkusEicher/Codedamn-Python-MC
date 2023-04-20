class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print("Hello, my name is", self.name)

p1 = Person("Markus", 25)
p2 = Person("Christoph", 30)

p1.say_hello() # Output: Hello, my name is Markus
p2.say_hello() # Output: Hello, my name is Christoph