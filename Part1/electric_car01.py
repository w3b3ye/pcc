#Inheritance Example showing passing a class instance as attributes

#Super Class (or Parent class)
class Car: #Define a class
    """My first Python class."""

    def __init__(self,make,model,year): #Init method of the class, though it is not necessary but recommended if using OOP
        """Initialize attributes for a car."""
        self.make = make #This and below attributes are initialized based on the parameters provided at the time of initializing class 
        self.model = model
        self.year = year

        self.odo_reading = 0 #Attributes with a default value

    def get_descriptive_name(self): #A method to print car name
        """Return a formatted name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odo(self):
        print(f"This car has {self.odo_reading} miles on it.")

    def update_odo(self,mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the value back.
        """
        if mileage >= self.odo_reading:
            self.odo_reading = mileage
        else:
            print("You can not roll back the odo reading.")

    def incre_odo(self,miles):
        self.odo_reading += miles #Same as self.odo_reading = self.odo_reading + miles
    

#Sub Class (or child class)

class Battery:
    """A simple example to model a battery for an electric car."""

    def __init__(self,battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def desc_battery(self):
        """Print a statement desc the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge.")

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        self.battery = Battery() #Passing a Battery class instance as attribute 

my_tesla = ElectricCar('tesla','model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.desc_battery()
my_tesla.battery.get_range()