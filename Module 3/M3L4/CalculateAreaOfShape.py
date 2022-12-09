"""Create a script called CalculateAreaOfShape.py. 
In the script, create a function called calculate_area_of_shape. 
The function should receive five arguments. 
The first argument should define what shape's area needs to be calculated, 
e.g. "Square". The other four arguments should be used to send measurements 
for length, height, width and radius. These four arguments should default to the value 0 if not used. 
Your function should calculate the area of at least three different shapes, e.g. square, cube and circle. 
In the main section of your script, demonstrate the calculation of the area of three shapes. 
Your function calls should make use of named arguments."""

from math import pi

def calculate_area_of_shape(shape_area, length=0, heigth=0, width=0, radius=0):
    if shape_area == 'Square':
        return length * heigth
    elif shape_area == 'Circle':
        return radius * radius * pi
    elif shape_area == 'Cube':
        return 6 * (length ** 2) 

area = calculate_area_of_shape('Square', length=10, heigth=10)
print(area)
area = calculate_area_of_shape('Circle', radius=25)
print(area)
area = calculate_area_of_shape('Cube', length=10)
print(area)
