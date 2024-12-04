# Base class
class ElectronicDevice:
    def __init__(self, brand, power_status=False):
        self.__brand = brand
        self.__power_status = power_status

    def get_brand(self):
        return self.__brand

    def get_power_status(self):
        return self.__power_status

    def power_on(self):
        self.__power_status = True
        print(f"{self.__brand} device is now ON.")

    def power_off(self):
        self.__power_status = False
        print(f"{self.__brand} device is now OFF.")

    def display_info(self):
        status = "ON" if self.__power_status else "OFF"
        print(f"Brand: {self.__brand}")
        print(f"Power Status: {status}")


# Derived class - Laptop
class Laptop(ElectronicDevice):
    def __init__(self, brand, ram_size, storage_size):
        super().__init__(brand)
        self.__ram_size = ram_size
        self.__storage_size = storage_size

    def get_ram_size(self):
        return self.__ram_size

    def set_ram_size(self, ram_size):
        self.__ram_size = ram_size

    def get_storage_size(self):
        return self.__storage_size

    def set_storage_size(self, storage_size):
        self.__storage_size = storage_size

    def display_info(self):
        super().display_info()
        print(f"RAM Size: {self.__ram_size}GB")
        print(f"Storage Size: {self.__storage_size}GB")


# Derived class - Smartphone
class Smartphone(ElectronicDevice):
    def __init__(self, brand, camera_resolution, battery_life):
        super().__init__(brand)
        self.__camera_resolution = camera_resolution
        self.__battery_life = battery_life

    def get_camera_resolution(self):
        return self.__camera_resolution

    def set_camera_resolution(self, camera_resolution):
        self.__camera_resolution = camera_resolution

    def get_battery_life(self):
        return self.__battery_life

    def set_battery_life(self, battery_life):
        self.__battery_life = battery_life

    def display_info(self):
        super().display_info()
        print(f"Camera Resolution: {self.__camera_resolution}MP")
        print(f"Battery Life: {self.__battery_life} hours")


# Create instances
laptop1 = Laptop("Dell", 16, 512)
smartphone1 = Smartphone("Samsung", 108, 24)

# Access and modify properties
laptop1.set_ram_size(32)
smartphone1.set_battery_life(30)

# Display electronic device information
laptop1.display_info()
smartphone1.display_info()
