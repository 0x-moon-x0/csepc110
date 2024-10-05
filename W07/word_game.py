secret = "crimson"
guess = ""
count = 0

print ("Welcome to the word guessing game!\n")
print ()

while guess.lower() != secret:

    guess = input ("What is your guess? ")

    if guess != secret:

        print ("Your guess was not correct.")
        count += 1
    else:

        print ("Congratulations! You guessed it!")
        count += 1

print (f"It took you {count} guesses.")