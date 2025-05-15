# Base class
class Person:

# name ko set karne wala constructor    
    def __init__(self, name):
        self.name = name

# Derived class Teacher

class Teacher(Person):
    def __init__(self, name, subject):

# super() ka use karke base class ka constructor call kiya
        super().__init__(name)
        # subject field ko set kiya
        self.subject = subject

    def show_info(self):

# blank line for better readability
      
       print()

# teacher ka naam aur subject print karne wala method

        print(f"Name: {self.name}")
        print(f"Subject: {self.subject}")

# Object banakar test karte hain

t1 = Teacher("Miss Warda", "Mathematics")
t1.show_info()
