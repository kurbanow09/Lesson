total = 0
count = 0

while True:
    user_input = input("Enter a number: ")
    if user_input == "0":
        break
    number = float(user_input)
    total += number
    count += 1
if count > 0:
    average = total / count
    print(f"The average of the numbers is: {average}")
else:
    print("No numbers were entered.")