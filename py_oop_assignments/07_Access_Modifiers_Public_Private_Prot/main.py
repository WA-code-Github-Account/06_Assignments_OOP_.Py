# Employee class banate hain

class Employee:


# Constructor ke through variables initialize kar rahe hain

    def __init__(self, name, salary, ssn):
        self.name = name          # Public variable (kisi bhi jaga se access ho sakta hai)
        self._salary = salary     # Protected variable (sirf andar ya inherited class se use karna chahiye)
        self.__ssn = ssn          # Private variable (bahar se direct access nahi hoga)

# Private variable ko access karne ke liye method banaya

    def show_private_info(self):
        print(f"Private SSN internally : {self.__ssn}")  # ye method andar se private data show karta hai


# Employee ka object banaya

emp = Employee("Aziza", 50000, "123-45-6789")

# blank line for better readability        
       
print()



# Public variable ko access karna (ye directly accessible hai)

print("Public name:", emp.name)

# Protected variable ko access karna (ye accessible hai, lekin use protected tareeqay se karna chahiye)

print("Protected salary:", emp._salary)

# Private variable ko direct access karne ki koshish (ye error dega)

try:
    print("Private SSN:", emp.__ssn)
except AttributeError:
    print("❌ Cannot access __ssn directly (private variable)")

# Private variable ko andar se access kar rahe hain method ke zariye

emp.show_private_info()
