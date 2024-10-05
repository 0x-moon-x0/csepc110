print ("Please enter the items of the shopping list (type 'quit' to finish):")
items = []
user_input = ""

while user_input != "quit":

    user_input = input ("Item: ")

    if user_input != "quit":

        items.append (user_input)

print ("The shopping list is:")

for item in items:

    print (item)

print ("The shopping list with indexes is:")

for i in range(len(items)):

    item = items [i]

    print (f"{i}. {item}")

change = int(input ("Which item would you like to change? "))
new_item = input ("What is the new item? ")

items[change] = new_item

for i in range(len (items)):
    item = items [i]

    print (f"{i}. {item}")