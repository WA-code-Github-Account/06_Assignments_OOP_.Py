from abc import ABC, abstractmethod

# Abstract class banai ja rahi hai jiska naam Shape hai
class Shape(ABC):


# area naam ka abstract method banaya gaya hai
    @abstractmethod
    def area(self):
        pass


# Rectangle class, Shape ko inherit kar rahi hai
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

# area method ko yahan implement kiya gaya hai
    def area(self):
        return self.width * self.height
    

# Rectangle ka object banaya gaya hai
rectangle = Rectangle(5, 3)


# blank line for better readability        
print()


# Area calculate karke print kiya ja raha hai
print("Area of the rectangle is:", rectangle.area())
