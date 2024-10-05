#word = "commitment"

#favorite_letter = input ("What is your favorite letter? ")

#for letter in word:

    #if letter.lower() == favorite_letter.lower():
        #print ("_", end="")
    #else:
        #print (letter.lower(), end="")

quote = "In coming days, it will not be possible to survive spiritually without the guiding, directing, comforting, and constant influence of the Holy Ghost."

restart = "yes"

while restart == "yes":

    number = int(input("Please enter a number: "))
    print ()

    for i, letter in enumerate(quote):

        if i % number == 0:
            print (letter.upper(), end="")
        else:
            print (letter.lower(), end="")

    print ()

    restart = input ("Would you like to try again? ")
    print ()

print ("Goodbye!")