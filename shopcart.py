cart = {}

print("""
S-Mart Options
================
1. Add Item
2. Remove Item
3. View Cart
4. Checkout
""")

option = int(input("How can we help you today? "))

while option != 4:
    if option == 1:
        item = input("Enter an item: ")
        if item in cart:
            print("Item is already in cart")
            qty = int(input("How many would you like to add? "))
            cart[item] += qty
        else:
            qty = int(input("Enter the quantity: "))
            cart[item] = qty
    elif option == 2:
        item = input("Enter an item: ")
        if item in cart:
            qty = int(input("How many would you like to remove? "))
            cart[item] -= qty
            if cart[item] <= 0:
                del(cart[item])
            else:
                print(f"{item} quantity is now {cart[item]}").title()
        else:
            print("I'm sorry, this item is not in your cart.")
    elif option == 3:
        for item in cart:
            print(item, ":", cart[item])
    elif  option != 4: 
        print("Enter a valid number please.")

    option = int(input("\n\nEnter an option: "))
else:
    print("Shop smart. Shop S-Mart!")