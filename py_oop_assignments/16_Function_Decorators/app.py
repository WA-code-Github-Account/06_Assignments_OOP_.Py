# Decorator function jo function call hone se pehle message print karega
def log_function_call(func):


# Wrapper function jo actual function ko call karega
    def wrapper():
        print("\nFunction is being called")  # Yeh message har function call se pehle print hoga
        func()  # Yeh line original function ko call karegi
    return wrapper  # Wrapper ko return karenge


# say_hello function par decorator apply kar rahe hain
@log_function_call
def say_hello():
    print("Hello!")  # Yeh message actual function ka output hai


# Ab decorated function ko call karenge
say_hello()  # Function call hone par sabse pehle message print hoga






# function decorators in oop method
# OOP Class: BankAccount
class BankAccount:
    def __init__(self, name, balance):
        self.name = name  # Account holder ka naam
        self.balance = balance  # Account ka initial balance


# Function decorator jo log karega transactions
    def log_transaction(func):
        def wrapper(self, amount):
            print(f"Logging transaction for {self.name}...")
            return func(self, amount)  # Actual function ko call karenge
        return wrapper
    

# Withdraw method par decorator apply kar rahe hain
    @log_transaction  # Is decorator ko apply kar rahe hain
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")
        else:
            print("Insufficient funds!")


# BankAccount ka object create kar rahe hain
account = BankAccount("Aziza", 100000)


# Account se paise withdraw karte hain, decorator pehle execute hoga
account.withdraw(2000)  # Function call ke time decorator log karega

