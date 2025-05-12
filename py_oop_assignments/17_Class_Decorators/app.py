# Yeh decorator class ko modify karega
def add_greeting(cls):


# Class ke andar aik new method add karte hain
    def greet(self):
        return "\n Hello from Decorator!"
    
    
# greet method ko class mein daal dete hain
    cls.greet = greet

    
# Modified class ko wapas return karte hain
    return cls


# Decorator ko use kar ke class define kar rahe hain
@add_greeting
class Person:
    def __init__(self, name):
        self.name = name


# Object banate hain aur greet method test karte hain
p = Person("Ali")

print(p.greet())  # Output: Hello from Decorator!
