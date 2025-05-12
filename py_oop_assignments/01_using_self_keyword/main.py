# Step 1: Student naam ki class banate hain

class Student:
    
# Step 2: Constructor __init__ banate hain jisme self, name, aur marks aayenge

    def __init__(self, name, marks):
        self.name = name  # object ka name set kar rahe hain
        self.marks = marks  # object ke marks set kar rahe hain

# Step 3: Method display() banate hain jo student details print karega

    def display(self):
        print("\nStudent Name:", self.name)
        print("Marks:", self.marks)

# blank line for better readability        
       
        print()


# Step 4: 3 students ke objects banate hain

# Fist student (s1)

s1 = Student("Aziza", 95)

# Secound student (s2)

s2 = Student("Warda", 92)

# Third student (s3)

s3 = Student("Ahmed", 78)


# Step 5: Har student ka display() method call karte hain

s1.display()  # Aziza ke details
s2.display()  # Warda ke details
s3.display()  # Ahmed ke details
