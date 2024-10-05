import math

pi = math.pi

def compute_area_square (side):

    area_square = side ** 2
    return area_square

# does the same thing, but using the rectangle function
# pretty pointless imo

# def compute_area_square (side):
#    area = compute_area_rectangle (side, side)
#    return area

def compute_area_rectangle (length, width):

    area_rectangle = length * width
    return area_rectangle

def compute_area_circle (radius):

    area_circle = pi * (radius ** 2)
    return area_circle

print ()
print ("Welcome to the area calculator! Type 'quit' to exit.")

choice = ""

while choice.lower() != "quit":

    print ()
    choice = input ("What shape do you have? ")

    choice = choice.lower()
    print ()

    if choice == "square":

        side_square = float (input ("What is the length of a side of the square? "))

        area_square = compute_area_square (side_square)

        print ()
        print (f"The area of the square is: {area_square:.2f}")

    elif choice == "rectangle":

        length_rectangle = float (input ("What is the length of the rectangle? "))
        width_rectangle = float (input ("What is the width of the rectangle? "))

        area_rectangle = compute_area_rectangle (length_rectangle, width_rectangle)

        print ()
        print (f"The area of the rectangle is: {area_rectangle:.2f}")
    
    elif choice == "circle":

        radius_circle = float (input ("What is the radius of the circle? "))

        area_circle = compute_area_circle (radius_circle)

        print ()
        print (f"The area of the circle is: {area_circle:.2f}")
   
print ("Goodbye.")