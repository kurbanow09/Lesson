total = 0
phone_number = input("Enter your phone number: ")

while True:
    payment = input("Please pay: ")
    if payment == "quit":
        break
    total += int(payment)
    print(f"You paid {total} manats!")
    print(f"{total} manats were transferred to {phone_number}")