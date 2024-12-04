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

# Creating an object of the Car class
my_car = Car("Honda", "Civic", 2018)

# Using the methods of the Car class
print("Car Information:")
print(my_car.get_car_info())

print("\nStarting Engine:")
my_car.start_engine()

print("\nStopping Engine:")
my_car.stop_engine()
