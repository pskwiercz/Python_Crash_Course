class Dog:
    """ Class Dog """

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is sitting")

    def roll_over(self):
        print(f"{self.name} is rolling over")


dog = Dog("Willie", 10)
dog.sit()
dog.roll_over()

class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading: int = 0 # Default value for parameter

    def get_descriptive_name(self) -> str:
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self) -> None:
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage) -> None:
        """Set the odometer reading to the given value."""
        self.odometer_reading = mileage

    def fill_gas_tank(self):
        print("This car got gas.")

car = Car('audi', 'a4', 2024)
print(car.get_descriptive_name())
car.read_odometer()
car.update_odometer(23)
car.read_odometer()

class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=40):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        self.battery = Battery() # composition


    def fill_gas_tank(self):
        print("This have not tank gas.")

my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()

my_leaf.fill_gas_tank()
car.fill_gas_tank()