def basic_calculator():
    while True:
        try:
            num1 = float(input("1-nji sany giriziň: "))
            num2 = float(input("2-nji sany giriziň: "))
        except ValueError:
            print("Nädogry san girizdiňiz. Täzeden synanyşyň.")
            continue

        print("Funksiýany saýlaň: '+', '-', '*', '/'")
        operation = input("Funksiýa: ")

        if operation not in ['+', '-', '*', '/']:
            print("Nädogry funksiýa!")
            continue

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                print("0-a bölüp bolmaýar!")
                continue
            result = num1 / num2

        print(f"Netije: {result}")

        again = input("Täzeden hasaplaýarsyňyzmy? (hawa/ýok): ").strip().lower()
        if again != 'hawa':
            print("Hasaplama maşyny tamamlandy.")
            break


basic_calculator()