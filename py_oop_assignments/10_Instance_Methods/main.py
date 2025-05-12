# Dog naam ki class banai ja rahi hai
class Dog:


# Constructor banaya gaya hai jisme name aur breed pass hote hain
    def __init__(self, name, breed):
        self.name = name  # Dog ka name assign ho raha hai
        self.breed = breed  # Dog ki breed assign ho rahi hai

# bark naam ka instance method banaya gaya hai
    def bark(self):

  
# blank line for better readability        
        print()      


# Dog ka name aur breed use karke ek message print kiya ja raha hai
        print(f"{self.name} is a German Shepherd and it is barking! Woof woof!")



# Dog ka aik object create kiya gaya hai
my_dog = Dog("Tommy", "German Shepherd")


# bark method call kiya ja raha hai
my_dog.bark()
