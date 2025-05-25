def add_greetings(cls):
    def greet(self):
        return "Hello from Decorator!"
    
    # adding greet method to the class
    cls.greet= greet
    return cls
# applying class decorator to the person class
@add_greetings
class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        return f"Hi, I am {self.name}."

    #creating an instance of the class
person = Person("Alice")    

# calling the greet method added by the decorator
print(person.greet()) # Output: Hello from Decorator!
print(person.introduce()) # Output: Hi, I am Alice.

