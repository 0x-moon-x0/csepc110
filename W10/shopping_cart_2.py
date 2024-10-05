print ()
print ("Welcome to the Shopping Cart Program!")

items = []
prices = []

menu_selection = 0

while menu_selection != 6:

    print ()
    print ("Please select one of the following:")
    print ("1. Add item")
    print ("2. View cart")
    print ("3. Remove item")
    print ("4. Change item")
    print ("5. Compute total")
    print ("6. Quit")
    
    print ()
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

        for i in range (len (items)):

            item = items [i]
            price = prices [i]

            print (f"{i}. {item} - ${price:.2f}")

    elif menu_selection == 3:

        print ()
        remove = int (input ("Which item would you like to remove? "))
        items.pop (remove)
        prices.pop (remove)

    elif menu_selection == 4:

        print ()
        edit = int (input ("Which item would you like to change? "))
        new_item = input ("What is the new name for the item? ")
        new_price = float (input ("What is the new price for the item? "))

        items [edit] = new_item
        prices [edit] = new_price

    elif menu_selection == 5:

        print ()
        total = sum (prices)
        print (f"The total price of the items in the shopping cart is ${total:.2f}")

    elif menu_selection == 6:

        print ()
        print ("Thank you. Goodbye.")

    else:
        print ()
        print ("Please enter a valid number.")