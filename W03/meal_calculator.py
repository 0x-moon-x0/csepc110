# entering values

price_child = float (input("What is the price of a child's meal? "))
price_adult = float (input("What is the price of an adult's meal? "))
child_count = int (input("How many children are there? "))
adult_count = int (input("How many adults are there? "))
tax_rate = float (input("What is the sales tax rate? "))
print ()

# calculating subtotal

subtotal = (price_child * child_count) + (price_adult * adult_count)
print (f"Subtotal: ${subtotal:.2f}")

# calculating sales tax

sales_tax = (subtotal * tax_rate) / 100
print (f"Sales tax: ${sales_tax:.2f}")

# calculating total

total = subtotal + sales_tax
print (f"Total: ${total:.2f}")
print ()


# payment and change

payment = float (input("What is the payment amount? "))
change = payment - total
print (f"Change: ${change:.2f}")

# offering a bag

bag = input ("Do you need a bag (yes or no)? ")
if bag.lower() == "yes":
    with_bag = change - 0.50
    print (f"Your change with a bag: ${with_bag:.2f}")
else:
    print ("Thank you for your purchase.")