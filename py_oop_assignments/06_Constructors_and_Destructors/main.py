# Logger class banai hai jo object create aur destroy hone par message dega

class Logger:

# Constructor method (__init__) — jab object banega to yeh chalega

    def __init__(self, name):
        self.name = name  # object ka naam store kar rahe hain

# blank line for better readability 
   
        print()

        print(f"Logger '{self.name}' created.")  # object create hone ka message

# Destructor method (__del__) — jab object destroy hoga to yeh chalega

    def __del__(self):
        print(f"Logger '{self.name}' destroyed.")  # object destroy hone ka message


# Yahan object banaya ja raha hai 'Aziza' naam ka

log1 = Logger("Aziza")

# Yahan manually object ko destroy kar rahe hain using del

del log1  # is se __del__ method chalega
