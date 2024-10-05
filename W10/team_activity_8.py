# creating lists and the initial variable to update the names and balances lists

names = []
balances = []
name = None

print ("Enter the names and balances of bank accounts (type 'quit' when done)")
print ()

while name != "quit":

    name = input ("What is the name of this account? ")
      
      # if the user doesn't quit here, we continue on to determining the balance

    if name != "quit":

        balance = float (input("What is the balance? "))

        names.append (name)
        balances.append (balance) # append both lists

print ()
print ("Account Information:")

for i in range (len(names)):
    
    print (f"{i}. {names [i]} - ${balances [i]}")  # we print the general index of the data, then go through each item in both lists

total = sum (balances)  # i decided to use the sum function for the total
average = total / len (balances)

# i would've normally used the max function to find the greatest number in a list, but this time we need to show 2 lists on the same line

highest_name = None
highest_balance = -1

# here we go through each list by their indexes

for i in range (len(names)):

    name = names [i]
    balance = balances [i]
    
    # then, we determine which balance is the highest

    if balance > highest_balance:
       
        highest_balance = balance
        highest_name = name

print ()
print (f"Total: ${total:.2f}")
print (f"Average: ${average:.2f}")
print (f"Highest balance: {highest_name} - ${highest_balance:.2f}")

update = "yes"  # setting this to "yes" so that it can run the while loop

while update == "yes":

    print ()
    update = input ("Do you want to update an account? ")

    if update == "yes":

        index = int (input("What account index do you want to update? "))
        new_amount = float (input("What is the new amount? "))

        balances [index] = new_amount  # replacing the previous value with a new user input

    print ()
    print ("Account Information:")

    for i in range (len(names)):
    
        print (f"{i}. {names [i]} - ${balances [i]}")