# Step 1: Bank naam ki class banate hain

class Bank:

# Step 2: Class variable define karte hain

    bank_name = "Summit Bank"

# Step 3: Constructor banate hain (object-specific info ke liye)

    def __init__(self, account_holder):
        self.account_holder = account_holder  # individual ka naam

# Step 4: Class method banate hain jo class variable ko change karega

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name  # class variable update kar rahe hain

# Step 5: Method to display details

    def display(self):
        print(f"Account Holder: {self.account_holder}, Bank: {Bank.bank_name}")


# Step 6: 3 bank account holders ke objects banate hain

acc1 = Bank("Aziza")
acc2 = Bank("Warda")
acc3 = Bank("Asghar")

# Step 7: Sab ka initial bank name check karte hain

print("\nBefore changing bank name:")
acc1.display()
acc2.display()
acc3.display()

# Step 8: Ab class method se bank name change karte hain

Bank.change_bank_name("New Mezan Bank")

# Step 9: Dubara sab objects ka bank name check karte hain

print("\nAfter changing bank name:")
acc1.display()
acc2.display()
acc3.display()
