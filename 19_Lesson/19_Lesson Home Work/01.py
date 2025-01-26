def cafe_order_system():
    # Menu items with prices and stock
    menu = {
        "coffee": {"price": 3, "stock": 5},
        "tea": {"price": 2, "stock": 10},
        "sandwich": {"price": 5, "stock": 15},
        "cake": {"price": 4, "stock": 2}
    }

    # Order dictionary
    order = {}

    print("Welcome to the Cafe!\n")
    
    # Display the menu and take orders
    while True:
        # Show the updated menu with stock
        print("Menu:")
        for item, details in menu.items():
            print(f"{item.capitalize()} (Stock: {details['stock']}) - {details['price']} $")
        
        # Prompt user for an item
        item = input("\nEnter the item you want to order or 'done' to finish: ").lower()
        if item == 'done':
            break
        
        # Validate the item
        if item in menu:
            # Validate the quantity
            quantity_input = input("Enter the quantity: ")
            if quantity_input.isdigit():
                quantity = int(quantity_input)
                if quantity <= menu[item]["stock"]:
                    order[item] = order.get(item, 0) + quantity
                    menu[item]["stock"] -= quantity
                    print(f"{quantity} {item}(s) added to your order.\n")
                    # If stock is depleted, remove item from menu
                    if menu[item]["stock"] == 0:
                        del menu[item]
                else:
                    print(f"Sorry, only {menu[item]['stock']} {item}(s) are available.\n")
            else:
                print("Invalid quantity. Please enter a valid number.\n")
        else:
            print("Invalid item or item is out of stock. Please choose from the menu.\n")
    
    # Calculate the total amount
    print("\nYour Order:")
    total = 0
    for item, quantity in order.items():
        cost = quantity * menu[item]["price"] if item in menu else quantity * (3 if item == "coffee" else 2 if item == "tea" else 5 if item == "sandwich" else 4)
        total += cost
        print(f"{item.capitalize()} x{quantity}: {cost} $")
    
    print(f"\nTotal Amount: {total} $")
    print("Thank you for your order!")

# Run the cafe order system
cafe_order_system()