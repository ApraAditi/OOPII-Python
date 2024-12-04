class Vehicle:
    def __init__(self, make, model):
        print("Vehicle Constructor")
        self.make = make
        self.model = model

    def display(self):
        print(f"Make: {self.make}, Model: {self.model}")

class Car(Vehicle):
    def __init__(self, make, model, year):
        print("Car Constructor")
        super().__init__(make, model)
        self.year = year

    def display(self):
        print(f"Car: {self.year} {self.make} {self.model}")

class Bike(Vehicle):
    def __init__(self, make, model, type_of_bike):
        print("Bike Constructor")
        super().__init__(make, model)
        self.type_of_bike = type_of_bike

    def display(self):
        print(f"Bike: {self.make} {self.model}, Type: {self.type_of_bike}")

class Truck(Vehicle):
    def __init__(self, make, model, capacity):
        print("Truck Constructor")
        super().__init__(make, model)
        self.capacity = capacity

    def display(self):
        print(f"Truck: {self.make} {self.model}, Capacity: {self.capacity} tons")

class ElectricCar(Car):
    def __init__(self, make, model, year, battery_capacity):
        print("ElectricCar Constructor")
        super().__init__(make, model, year)
        self.battery_capacity = battery_capacity

    def display(self):
        print(f"Electric Car: {self.year} {self.make} {self.model}, Battery Capacity: {self.battery_capacity} kWh")

class DieselTruck(Truck):
    def __init__(self, make, model, capacity, fuel_efficiency):
        print("DieselTruck Constructor")
        super().__init__(make, model, capacity)
        self.fuel_efficiency = fuel_efficiency

    def display(self):
        print(f"Diesel Truck: {self.make} {self.model}, Capacity: {self.capacity} tons, Fuel Efficiency: {self.fuel_efficiency} km/l")

# Creating instances and displaying details
car1 = Car("Toyota", "Camry", 2020)
car1.display()

bike1 = Bike("Yamaha", "MT-07", "Sport")
bike1.display()

truck1 = Truck("Volvo", "FH16", 30)
truck1.display()

e_car1 = ElectricCar("Tesla", "Model S", 2021, 100)
e_car1.display()

d_truck1 = DieselTruck("Scania", "R500", 20, 3)
d_truck1.display()
