total_sum = 0

while True:
    user_input = input("Enter a number: ")
    if user_input == "0":
        break
    if user_input.isdigit():
        total_sum += int(user_input)
else:
    print("Please enter a valid number or type '0' to exit")

print(f"Sum: {total_sum}")