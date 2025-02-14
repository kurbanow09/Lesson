with open("sanlar.txt", "w") as file:
    i = 1
    while i <= 5:
        num = int(input(f"{i}-san: "))
        i += 1
        file.write(f"{num}   ")