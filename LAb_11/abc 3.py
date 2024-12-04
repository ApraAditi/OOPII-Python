from abc import ABC, abstractmethod

# Abstract base class
class Appliance(ABC):
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    @abstractmethod
    def display_features(self):
        pass

    @abstractmethod
    def energy_consumption(self):
        pass

    def display_info(self):
        print(f"Appliance Brand: {self.brand}")
        print(f"Model: {self.model}")

# Derived class - WashingMachine
class WashingMachine(Appliance):
    def __init__(self, brand, model, load_capacity, spin_speed):
        super().__init__(brand, model)
        self.load_capacity = load_capacity
        self.spin_speed = spin_speed

    def display_features(self):
        print(f"Load Capacity: {self.load_capacity} kg")
        print(f"Spin Speed: {self.spin_speed} RPM")

    def energy_consumption(self):
        return f"Energy Consumption: {self.load_capacity * 0.5} kWh per wash"

# Derived class - Refrigerator
class Refrigerator(Appliance):
    def __init__(self, brand, model, capacity, has_freezer):
        super().__init__(brand, model)
        self.capacity = capacity
        self.has_freezer = has_freezer

    def display_features(self):
        print(f"Capacity: {self.capacity} liters")
        print(f"Freezer: {'Yes' if self.has_freezer else 'No'}")

    def energy_consumption(self):
        return f"Energy Consumption: {self.capacity * 0.3} kWh per day"

# Creating instances of WashingMachine and Refrigerator
washer = WashingMachine("LG", "TwinWash", 7, 1400)
fridge = Refrigerator("Samsung", "CoolTech", 300, True)

# Displaying information and calling abstract methods
appliances = [washer, fridge]
for appliance in appliances:
    appliance.display_info()
    appliance.display_features()
    print(appliance.energy_consumption())
    print()
