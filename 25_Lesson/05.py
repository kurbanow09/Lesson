with open ("students.txt", "a") as fayl:
    for i in range(5):
        a = input(f"{i + 1} - ady: ")
        fayl.write(f"{i + 1}-{a}\n")
