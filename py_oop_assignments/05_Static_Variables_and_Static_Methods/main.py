# Step 1: MathUtils class banate hain

class MathUtils:

# Step 2: Static method banate hain jisme 'self' ya 'cls' nahi hota

    @staticmethod
    def add(a, b):
        return a + b  # sirf 2 numbers ka sum return karega


# Step 3: Static method ko directly class se call karte hain

result1 = MathUtils.add(5, 3)
result2 = MathUtils.add(10, 20)

# Step 4: Results print karte hain

print()  # blank line for better readability
print("5 + 3 =", result1)  
print("10 + 20 =", result2)
