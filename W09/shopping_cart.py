print ()
print ("Welcome to the Shopping Cart Program!")

items = []
prices = []

menu_selection = 0

while menu_selection != 5:

    print ()
    print ("Please select one of the following:")
    print ("1. Add item")
    print ("2. View cart")
    print ("3. Remove item")
    print ("4. Compute total")
    print ("5. Quit")
    
    menu_selection = int (input ("Please enter an action: "))

    if menu_selection == 1:

        print ()
        item = input ("What item would you like to add? ")
        items.append (item)

        price = float (input (f"What is the price of '{item}'? "))
        prices.append (price)

        print (f"'{item}' has been added to your cart.")

    elif menu_selection == 2:

        print ()
        print ("The contents of the shopping cart are:")
        print ()

        for item in items:
            print (item)

    elif menu_selection == 4:

        print ()
        total = sum (prices)
        print (f"The total price of the items in the shopping cart is ${total:.2f}")

    elif menu_selection == 5:

        print ()
        print ("Thank you. Goodbye.")

    else:
        print ()
        print ("Please enter a valid number.")
