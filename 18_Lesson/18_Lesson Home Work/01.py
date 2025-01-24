products = {
    "milk": {"category": "drinks", "price": 4},
    "bread": {"category": "bakery", "price": 2},
    "apple": {"category": "fruits", "price": 3},
    "egg": {"category": "dairy and protein", "price": 5},
    "cheese": {"category": "dairy", "price": 6},
    "sausage": {"category": "meat", "price": 8},
}

while True:
    print("\nProducts and their prices:")
    for product, info in products.items():
        print(f"- {product} ({info['category']}): {info['price']} TMT")
    
    product = input("\nEnter the product you want to buy or type 'done' to finish: ").lower()
    
    if product == "done":
        break

    if product in products:
        quantity = input("Enter the quantity: ")
        if quantity.isdigit():
            quantity = int(quantity)
            total_cost = products[product]["price"] * quantity
            print(f"\n{product} x{quantity}: {total_cost} TMT")
        else:
            print("Invalid quantity. Please enter a valid number.")
    else:
        print("Sorry, that product is not available. Please choose another.")