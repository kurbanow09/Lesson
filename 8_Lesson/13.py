num_count = int(input("How many numbers input: "))
total_sum = 0
for i in range(1, num_count + 1):
    number = int(input(f"{i} number : "))
    total_sum += number
print("Sum: ", total_sum)