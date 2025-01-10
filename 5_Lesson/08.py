num = int(input("Enter a number: "))
if num % 2 == 0 and num < 10:
    print("one digit, even")
elif num % 2 == 1 and num < 10:
    print("one digit, odd")
elif num % 2 == 1 and num < 100:
    print("two digit, odd")
elif num % 2 == 1 and num < 100:
    print("two digit, even")
elif num % 2 == 1 and num < 1000:
    print("three digit, even")
elif num % 2 == 1 and num < 1000:
    print("three digit, odd")
elif num >= 999:
    print("blmk")
