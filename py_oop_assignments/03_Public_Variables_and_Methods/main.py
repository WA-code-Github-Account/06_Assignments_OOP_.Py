# Step 1: Car naam ki class banate hain

class Car:

# Step 2: Constructor banate hain jisme brand set karenge

    def __init__(self, brand):
        self.brand = brand  # yeh ek public variable hai

# Step 3: Public method start() banate hain

    def start(self):
        print(self.brand, "Car is starting...")  # brand use kar rahe hain


# Step 4: Class ka object banate hain

my_car = Car("Toyota")

# Step 5: Public variable ko bahar se access karte hain

print("\nCar Brand:", my_car.brand)

# Step 6: Public method ko call karte hain

my_car.start()
