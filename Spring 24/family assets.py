class FamilyMember:
    def __init__(self, name):
        self.name = name
        self.assets = 0

    def add_assets(self, amount):
        self.assets += amount

    def get_assets(self):
        return self.assets


class Grandfather(FamilyMember):
    def __init__(self, name, estate_value):
        super().__init__(name)
        self.estate_value = estate_value

    def pass_estate_to_father(self, father):
        father.add_assets(self.estate_value)


class Father(FamilyMember):
    def __init__(self, name, land, flats, cars, bank_savings, donation_percentage):
        super().__init__(name)
        self.land = land
        self.flats = flats
        self.cars = cars
        self.bank_savings = bank_savings
        self.donation_percentage = donation_percentage
        self.add_assets(land + flats + cars + bank_savings)

    def calculate_donation(self):
        donation = (self.land + self.bank_savings) * self.donation_percentage
        return donation

    def distribute_assets(self, son, daughter):
        remaining_assets = self.assets - self.calculate_donation()
        son_share = (2 / 3) * remaining_assets
        daughter_share = (1 / 3) * remaining_assets

        son.add_assets(son_share)
        daughter.add_assets(daughter_share)


class Child(FamilyMember):
    pass


# Initialize family members
grandfather = Grandfather("Grandfather", estate_value=500000)
father = Father("Father", land=200000, flats=150000, cars=50000, bank_savings=100000, donation_percentage=0.1)
son = Child("Son")
daughter = Child("Daughter")

# Step 1: Grandfather passes estate to the father
grandfather.pass_estate_to_father(father)

# Step 2: Father calculates donation and distributes remaining assets
donation = father.calculate_donation()
father.distribute_assets(son, daughter)

# Display results
print(f"{grandfather.name}'s Total Assets: {grandfather.get_assets()}")
print(f"{father.name}'s Total Assets: {father.get_assets()}")
print(f"Donation to Charity: {donation}")
print(f"{son.name}'s Total Assets: {son.get_assets()}")
print(f"{daughter.name}'s Total Assets: {daughter.get_assets()}")
