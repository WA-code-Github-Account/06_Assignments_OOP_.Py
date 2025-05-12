# Base class A
class A:
    def show(self):
        print("This is show() from class A")

# Class B inherits from A
class B(A):
    def show(self):
        print("\nThis is show() from class B")

# Class C inherits from A
class C(A):
    def show(self):
        print("This is show() from class C")

# Class D inherits from both B and C
class D(B, C):
    pass  # D khud show() define nahi karta, inheritance use karega


# Creating object of class D
obj = D()


# Calling show() method
obj.show()  # Roman Urdu: Yeh method D ke MRO ke mutabiq resolve hoga


# Printing Method Resolution Order
print("MRO for class D:", D.__mro__)  # Roman Urdu: MRO batata hai kis order mein classes check hongi
