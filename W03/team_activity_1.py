# Rectangle Area
Rectangle_Length = float(input ('What is the length of the rectangle in cm? '))
Rectangle_Width = float(input('What is the width of the rectangle in cm? '))
Rectangle_Area = Rectangle_Length * Rectangle_Width
print(f'The area of the rectangle is: {Rectangle_Area} cm^2')
print()

# Square Area
Square_Length = float(input('What is the length of the square in cm? '))
Square_Area = Square_Length ** 2
print (f'The area of the square is: {Square_Area} cm^2')
print()

# Circle Area 
from math import pi
Circle_Radius = float(input ('What is the radius of the circle? '))
Circle_Area = pi * Circle_Radius ** 2
print (f'The area of the circle is: {Circle_Area}')
print ()

# Stretch Challenge 01

from math import pi
print (pi)

# Stretch Challenge 02

Length_Value = float(input ('Please enter the length value in cm (only numbers): '))
# Formula for the area of the square
Square_Area_1 = Length_Value ** 2
# Formula for the area of the circle
Circle_Area_1 = pi * Length_Value
# Formula for the volume of the cube
Cube_Volume = Length_Value ** 3
# Formula for the volume of the sphere
Sphere_Volume = 4/3 * pi * Length_Value ** 3

# Executing
print (f'The area of the square is: {Square_Area_1}')
print (f'The area of the circle is: {Circle_Area_1}')
print (f'The volume of the cube is: {Cube_Volume}')
print (f'The volume of the sphere is: {Sphere_Volume}')


