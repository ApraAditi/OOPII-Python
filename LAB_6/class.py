# Defining the Car class
class Car:
    def __init__(self, make, model, year):
        self.make = make  # Car's make (e.g., Toyota, Ford)
        self.model = model  # Car's model (e.g., Camry, Mustang)
        self.year = year  # Car's year of manufacture

    def start_engine(self):
        print(f"The engine of the {self.year} {self.make} {self.model} is now running.")

    def stop_engine(self):
        print(f"The engine of the {self.year} {self.make} {self.model} has been turned off.")

    def get_car_info(self):
        return f"{self.year} {self.make} {self.model}"


# Creating instances of the Car class
car1 = Car("Toyota", "Camry", 2020)
car2 = Car("Ford", "Mustang", 2021)

# Using the methods of the Car class
print("Car Information:")
print(car1.get_car_info())
print(car2.get_car_info())

print("\nStarting Engines:")
car1.start_engine()
car2.start_engine()

print("\nStopping Engines:")
car1.stop_engine()
car2.stop_engine()
