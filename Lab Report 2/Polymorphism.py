class Transport:
    def __init__(self, weight, distance):
        self.weight = weight
        self.distance = distance

    def calculate_cost(self):
        raise NotImplementedError("Subclasses must implement this method")

class Truck(Transport):
    def calculate_cost(self):
        # Truck cost calculation logic
        return self.weight * 10 + self.distance * 2

class Ship(Transport):
    def calculate_cost(self):
        # Ship cost calculation logic
        return self.weight * 5 + self.distance * 3

class Plane(Transport):
    def calculate_cost(self):
        # Plane cost calculation logic
        return self.weight * 20 + self.distance * 5

def calculate_delivery_costs(transports):
    for transport in transports:
        cost = transport.calculate_cost()
        print(f"Cost for {type(transport).__name__}: {cost}")

# Test data
transports = [
    Truck(100, 500),
    Ship(200, 1000),
    Plane(50, 2000)
]

calculate_delivery_costs(transports)