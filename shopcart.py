import random
#variables
cart = {}
totalcost = 0

posverbal = ["Perfect choice!", "You have excellent taste!", "How did you get so smart!"]
posphrase = random.choice(posverbal)

negverbal = ["They can't all be winners.","We understand. Everyone has a budget.","You should have known it was too many."]
negphrase = random.choice(negverbal)

def int_input(prompt):#check for invalid string inputs
    while True:
        try:
            edgecase = int(input(prompt))
            return edgecase
        except ValueError as x:
            print("Please enter a valid number.")
#menu
print("""
S-Mart Options
================
1. Add Item
2. Remove Item
3. View Cart
4. Checkout
""")

option = int(int_input("How can we help you today? "))
#main flow chart
while option != 4:   
    if option == 1:#adding
        item = input("What item would you like to add? ")
        if item in cart:#if item exists add to quantity
            print("Item is already in cart.")
            qty = int(int_input("How many would you like to add? "))
            cart[item][0] += qty
            print(f"There are now {cart[item][0]} {item} in your cart.")
        else:#add item to cart with quantity and cost - quack quack
            print(posphrase)
            qty = int(int_input("How many would you like to add? "))
            cost = float(input("How much does one of those cost? "))
            cart[item] = [qty, cost]
    elif option == 2:#removing
        item = input("Which item would you like to remove? ")
        if item in cart:#if item exists remove from quantity
            qty = int(int_input("How many would you like to remove? "))
            cart[item][0] -= qty
            if cart[item][0] <= 0:#if less than 1 remove item from list
                del(cart[item])
                print((negphrase) + " This item has been removed from your cart.")
            else:#if 1 or more show new value
                print(f"There are now {cart[item][0]} {item} in your cart")
        else:
            print("Apologies, this item is not in your cart.")
    elif option == 3:#view
        for item in cart:
            print(item, ":", cart[item][0], ":", cart[item][1])
        print("That's a lot of quality products! Unless it's empty, then hurry up and buy.")
    elif option != 4:#any invalid number input
        print("Enter a valid number please.")
#while not - directs back thru options
    option = print("""
S-Mart Options
================
1. Add Item
2. Remove Item
3. View Cart
4. Checkout
""")
    option = int(int_input("Please choose another option: "))
#checkout ticket
print("Shop smart. Shop S-Mart!")
for item in cart:
    print(f"{item} : {cart[item][0]} : {cart[item][1]}")
    totalcost = cart[item][0] * cart[item][1] + totalcost
tax = totalcost * .0625
grandtotal = tax + totalcost
print(f"""
Subtotal: ${totalcost:.2f}
Tax: ${tax:.2f}
Total: ${grandtotal:.2f}
""")