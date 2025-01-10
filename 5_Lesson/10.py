num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

if (num1 > num2 and num1 < num3) or (num1 < num2 and num1 > num3):
    mid_num = num1
elif (num2 > num1 and num2 < num3) or (num2 < num1 and num2 > num3):
    mid_num = num2
else:
    mid_num = num3

print(f"Mid number: {mid_num}")