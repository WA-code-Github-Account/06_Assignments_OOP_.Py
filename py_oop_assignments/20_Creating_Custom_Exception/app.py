# Custom exception class
class InvalidAgeError(Exception):

# Ye exception un logon ke liye hai jo 18 se kam age rakhte hain
    pass

# Person class define kar rahe hain
class Person:

# Constructor mein name aur age assign kar rahe hain.
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def check_age(self):

# Age check kar rahe hain ke kya 18 se kam hai
        if self.age < 18:

# Agar age kam hai to custom exception raise karenge
            raise InvalidAgeError("Age is below 18 — not allowed!")
        
        else:

# Agar age theek hai to welcome message show hoga
            print(f"Welcome {self.name}! Your age is valid.")

# Try-except block se error handle kar rahe hain
try:

# User se input le rahe hain
    p = Person("Aziza", int(input("\nEnter your age: ")))

    
# Age check karne ke liye method call kar rahe hain
    p.check_age()


except InvalidAgeError as e:


# Agar custom error raise ho to usay handle kar rahe hain
    print("Error:", e)

