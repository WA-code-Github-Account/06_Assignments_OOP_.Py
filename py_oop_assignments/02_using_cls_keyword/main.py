# Step 1: Class ka naam rakha hai Counter

class Counter:

# Step 2: Ek class variable banaya jisme count rakhenge (shared by all objects)

    object_count = 0

# Step 3: Constructor __init__ jab bhi object banega to count badhega

    def __init__(self):

# Jab bhi naya object banega, object_count increase hoga

        Counter.object_count += 1

# Step 4: Class method banaya jo cls ka use kare

    @classmethod
    def display_count(cls):

# cls ka matlab class khud

        print("\nTotal objects created:", cls.object_count)


# Step 5: Ab kuch objects banate hain

obj1 = Counter()  # 1st object
obj2 = Counter()  # 2nd object
obj3 = Counter()  # 3rd object

# Step 6: Class method call karte hain taake total count display ho

Counter.display_count()
