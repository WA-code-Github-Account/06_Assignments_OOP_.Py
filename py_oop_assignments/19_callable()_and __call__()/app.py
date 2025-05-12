# Ye ek class hai jo kisi bhi number ko ek given factor se multiply karegi
class Multiplier:

# Ye constructor method hai — jab bhi object banega, ye function automatic chalega    
    def __init__(self, factor):

    
# factor ko object ke andar store kar rahe hain (self.factor)
        self.factor = factor

# __call__ special method hai jo object ko function ki tarah use karne deta hai
    def __call__(self, number):


# Jab object ko () ke sath call karte hain, to ye method run hota hai
        return number * self.factor

# Multiplier class ka object bana rahe hain, jisme factor = 3 set kar rahe hain
m = Multiplier(3)

# blank line for better readability 
print()

# Check kar rahe hain kya 'm' callable hai (kya isay function ki tarah call kiya ja sakta hai?)
print(callable(m))  # Output: True

# Object ko function ki tarah call kar rahe hain, aur 5 ko 3 se multiply kara rahe hain
print(m(5))  # Output: 15 (kyunki 5 * 3 = 15)
