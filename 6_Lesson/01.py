print("""
1. (+)
2. (-)
3. (*)
4. (/)
""")

ha = int(input("Haysy amal: "))
num1 = int(input("Birinji sanyn: "))
num2 = int(input("Ikinji sanyn: "))

if ha == 1:
    print(f"{num1} + {num2} = {num1 + num2}")
elif ha == 2:
    print(f"{num1} - {num2} = {num1 - num2}")
elif ha == 3:
    print(f"{num1} * {num2} = {num1 * num2}")
elif ha == 3:
    print(f"{num1} / {num2} = {num1 / num2}")