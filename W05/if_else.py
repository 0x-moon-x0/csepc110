# asking for numbers

first = int (input ("What is the first number? "))
second = int (input ("What is the second number? "))

# conditioning

if first > second:
    print ("The first number is greater.")
else:
    print ("The first number is not greater.")

if first == second:
    print ("The numbers are equal.")
else:
    print ("The numbers are not equal.")

if second > first:
    print ("The second number is greater.")
else:
    print ("The second number is not greater.")

print ()

# asking for animal

animal = input ("What is your favorite animal? ")

# conditioning

if animal.lower() == "cow" \
    or animal.lower() == "bat":
    print ("That's my favorite animal too!")
else:
    print ("That one is not my favorite.")
