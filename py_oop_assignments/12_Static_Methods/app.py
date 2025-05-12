# TemperatureConverter class banai gayi hai jo OOP ke principles follow karti hai

class TemperatureConverter:
    
# Constructor (__init__) jo initial temperature set karta hai
    def __init__(self, celsius):
        self.celsius = celsius  # object-level temperature value store hoti hai


# Method 1: Static method for Celsius to Fahrenheit conversion
    @staticmethod
    def celsius_to_fahrenheit_static(c):
        return (c * 9/5) + 32  # formula lagaya gaya hai conversion ka
    

# Method 2: Instance method for Celsius to Fahrenheit conversion (OOP approach)
    def celsius_to_fahrenheit_instance(self):
        return (self.celsius * 9/5) + 32  # instance method now uses object temperature
    

# Method 1: Static method use karte hue
print("\nUsing Static Method:")
print("Fahrenheit value :", TemperatureConverter.celsius_to_fahrenheit_static(35))


# Method 2: OOP approach use karte hue with constructor
print("\nUsing OOP Method:")

converter = TemperatureConverter(35)  # Object create karte hue Celsius value pass ki

print("Fahrenheit value :", converter.celsius_to_fahrenheit_instance())  # Instance method call