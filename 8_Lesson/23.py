a = int(input("Enter A: "))
b = int(input("Enter B: "))
total_sum = 0
for i in range(a, b + 1):
    total_sum += i
print("Sum: ", total_sum)