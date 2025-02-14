with open("Numbers.txt", "w") as file:
    i = 1
    while i <= 7:
        num = int(input(f"{i}-san: "))
        i += 1
        file.write(f"{num}    ")