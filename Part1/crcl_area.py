class CrclArea:
    """Class to calclate the area of a circle."""
    def __init__(self, pi, radius):
        self.pi = pi
        self.radius = radius
    
    def crcl_area(self):
        area = self.pi * (self.radius)**2
        return area
    
       
pi = ''
radi = 2

file = 'pi_digits.txt'
with open(file) as file_object:
    lines = file_object.readlines() 
    for line in lines:
        pi += line.strip()

print(f"pi value given in the file is '{pi}'.")

calc_area = CrclArea(float(pi),radi)
print(f"Area of circle is '{calc_area.crcl_area()}'.")

