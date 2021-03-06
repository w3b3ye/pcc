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

    def update_odo(self,mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the value back.
        """
        if mileage >= self.odo_reading:
            self.odo_reading = mileage
        else:
            print("You can not roll back the odo reading.")
    
my_new_car = Car('audi','a4',2019) #Creating an instance of class "car"
print(my_new_car.get_descriptive_name()) #Calling the method of class car.
print(my_new_car.odo_reading) #Printing a attribute 

my_new_car.odo_reading = 10 #Assigning a new value to the attribute 
print(my_new_car.odo_reading)

#Changing odo reading using class method
my_new_car.update_odo(9) #This will print "You can not roll back the odo reading."
print(my_new_car.odo_reading) #This will print old value which is 10

my_new_car.update_odo(12)
print(my_new_car.odo_reading)

