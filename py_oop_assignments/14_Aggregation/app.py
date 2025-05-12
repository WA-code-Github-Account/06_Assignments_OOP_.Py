# Employee class bana rahay hain jo independently kaam karti hai
class Employee:
    def __init__(self, name, emp_id):
        self.name = name  # employee ka naam
        self.emp_id = emp_id  # employee ka ID



# Department class bana rahay hain jo Employee object ko refer karti hai (aggregation)
class Department:
    def __init__(self, dept_name, employee):
        self.dept_name = dept_name  # department ka naam
        self.employee = employee  # yahan pe existing Employee object ka reference pass kiya gaya hai

    def show_details(self):


# employee ki details department ke zariye show karwa rahay hain
        print(f"\nDepartment: {self.dept_name}")
        print(f"\nEmployee Name: {self.employee.name}")
        print(f"\nEmployee ID: {self.employee.emp_id}")


# pehlay ek Employee object banaya
emp1 = Employee("Aziza", 786)


# usi employee ko use karte huay Department object banaya (aggregation ka concept)
dept1 = Department("HR", emp1)


# details show kar rahay hain
dept1.show_details()
