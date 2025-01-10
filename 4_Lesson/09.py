num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
a = num1 % num2 == 0
b = num1 % num2 != 0
c = num1 % num2
if a :
    print(f"No, remainder {num1}")
elif b:
    print(f"Yes, remainder  \nThe remainder is {c}")