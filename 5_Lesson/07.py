num = int(input("Enter a number: "))
if num % 2 == 0 and num > 0:
    print("Positive, even")
elif num % 2 == 1 and num < 0:
    print("Negative, odd")
elif num % 2 == 0 and num < 0:
    print("Negative, even")
elif num % 2 == 1 and num > 0:
    print("Positive, odd")
elif num == 0:
    print("zero")
