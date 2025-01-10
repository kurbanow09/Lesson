number = int(input("Enter a number: "))
while number > 0:
    if number % 2 == 0:
        print(number, 'is a even number')
    else:
        print(number, 'is a odd number')
    number -= 1