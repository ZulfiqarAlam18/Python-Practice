import math
import getpass


radius = float(input("Enter radius of circle :"))

def areaOfCircle(radius):
    """"Fucntion for calculating area of circle"""
    return  math.pi*radius**2


print(f"The area of circle having radius of {radius} is :",areaOfCircle(radius))