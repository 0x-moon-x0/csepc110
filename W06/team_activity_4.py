# creating a boolean variable and setting it to "true"

can_ride = True

# asking for the information on the first rider

age_1 = int(input("What is the age of the first rider? "))

# checking whether the first rider has a golden passport

if age_1 >= 12 and age_1 < 18:
    has_passport_1 = input("Does the first rider own a Golden Passport (yes/no)? ")
else:
    print ("Because you aren't an owner of a Golden Passport, your age won't be considered as 18.")

height_1 = int(input("What is the height of the first rider? "))

# asking if there's a second rider

rider_2 = (input("Is there a second rider (yes/no)? "))

# if there is a second rider, i'm asking for their age and height

if rider_2.lower() == "yes":
    age_2 = int(input("What is the age of the second rider? "))

 # checking whether the second rider has a golden passport

    if age_2 >= 12 and age_2 < 18:
        has_passport_2 = input("Does the second rider own a Golden Passport (yes/no)? ")

    height_2 = int(input("What is the height of the second rider? "))

  # if either one of the riders is below 36 inches tall, they can't ride

    if height_1 < 36 or height_2 < 36:
        can_ride = False

      # if they're both over 36 inches tall, then at least one of them has to be 18 years old (or both of them have to be at least 12 years old and 52 inches tall)
    else:
        if age_1 >= 18 or age_2 >= 18 or has_passport_1.lower() == "yes" or has_passport_2.lower() == "yes":
            can_ride

         # if neither of them is 18 and over
        else:
            if age_1 >= 12 and height_1 >= 52 and age_2 >= 12 and height_2 >= 52:
                can_ride
            elif (age_1 >= 16 and age_2 >= 14) or (age_1 >= 14 and age_2 >= 16):
                can_ride
            else:
                can_ride = False

 # if there's only one rider, they have to be at least 18 years old and at least 62 inches tall
else:
    if (age_1 >= 18 or has_passport_1.lower() == "yes") and height_1 >= 62: 
        can_ride
    else:
        can_ride = False

# printing out the final decisions

if can_ride:
    print ("Welcome to the ride. Please be safe and have fun!")
else:
    print("Sorry, you may not ride.")