product_price = 5
payment = 0

while payment < product_price:
    remaining_amout = product_price - payment
    print(f"please pay {remaining_amout} more manats. ")
    new_payment = float(input("Amount to pay: "))
    payment += new_payment

    print("Payment completed. You can take your product. ")