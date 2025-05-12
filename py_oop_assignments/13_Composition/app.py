# Engine class jo ek method define karti hai
class Engine:
    def start(self):
        print("Engine is starting...")



# Car class jo Engine ka object apne andar store karti hai
class Car:
    def __init__(self, engine):
        self.engine = engine  # Car mein Engine ka object pass kiya jata hai

    
    def start_car(self):
        print("\nCar is starting...")
        self.engine.start()  # Car class ke through Engine ka method call karna


# Engine ka object create kar rahe hain
engine = Engine()


# Car ka object create karte hain aur engine ko pass karte hain
car = Car(engine)


# Car ko start karte hain
car.start_car()  # Car start hone par Engine ka method bhi call hoga
