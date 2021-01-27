class Car: #Define a class
    """My first Python class."""

    def __init__(self,make,model,year): #Init method of the class, though it is not necessary but recommended if using OOP
        """Initialize attributes for a car."""
        self.make = make
        self.model = model
        self.year = year


    def get_descriptive_name(self): #A method to print car name
        """Return a formatted name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
my_new_car = Car('audi','a4',2019) #Creating an instance of class "car"
print(my_new_car.get_descriptive_name()) #Calling the method of class car.