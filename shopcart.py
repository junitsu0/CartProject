cart = {}
totalcost = 0

def int_input(prompt):
    while True:
        try:
            edgecase = int(input(prompt))
            return edgecase
        except ValueError as x:
            print("Please enter a valid number.")

print("""
S-Mart Options
================
1. Add Item
2. Remove Item
3. View Cart
4. Checkout
""")

option = int(int_input("How can we help you today? "))

while option != 4:   
    if option == 1:
        item = input("Enter an item: ")
        if item in cart:
            print("Item is already in cart")
            qty = int(int_input("How many would you like to add? "))
            cart[item][0] += qty
            print(f"{item} quantity is now {cart[item]}")
        else:
            qty = int(int_input("Enter the quantity: "))
            cost = float(input("How much does it cost? "))
            cart[item] = [qty, cost]
    elif option == 2:
        item = input("Enter an item: ")
        if item in cart:
            qty = int(int_input("How many would you like to remove? "))
            cart[item][0] -= qty
            if cart[item][0] <= 0:
                del(cart[item])
            else:
                print(f"{item} quantity is now {cart[item]}")
        else:
            print("I'm sorry, this item is not in your cart.")
    elif option == 3:
        for item in cart:
            print(item, ":", cart[item][0], ":", cart[item][1])
    elif option != 4: 
        print("Enter a valid number please.")

    option = int(int_input("\n\nPlease choose another option: "))
  
print("Shop smart. Shop S-Mart!")
for item in cart:
    print(item, ":", cart[item][0], ":", cart[item][1])
    totalcost = cart[item][0] * cart[item][1] + totalcost
print(totalcost)