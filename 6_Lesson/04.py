while True:
    user_input = input("Enter a number: ")
    if user_input == "0":
        break
    if user_input.isdigit():
        number = int(user_input)
        print(f"{number} the square is {number ** 2}")
else:
    print("Please enter a valid number or type '0' to exit.")