import random

words = ["crimson", "pineapple", "tree", "cactus", "cattle", "beautiful", "golden", "spirit", "sap", "vet", "prepare", "sweet", "bubbles", "donut", "dragon", "quest", "cupcake", "pillar", "sound", "ship", "flowers", "create", "proud", "gnome"]
secret = random.choice(words)
count = 0
guess = input ("What is your guess? ").lower()
hint = "_ " * len(secret)

while guess != secret:

    print (f"Your hint is: {hint}")

    guess = input ("What is your guess? ").lower()

    hint = " "
    count += 1

    while len(guess) != len(secret):

        print ("Your guess doesn't have the same amount of characters as the secret word. Please try again.")

        guess = input ("What is your guess? ").lower()

        count += 1

    for i, letter in enumerate(guess):

        if guess [i] == secret [i]:

                hint += (letter.upper() + " ")

        elif guess [i] in secret:

            hint += (letter.lower() + " ")
        
        else:

            hint += "_ "

print ("Congratulations! You guessed the secret word!")

print (f"It took you {count} guesses.")






    
