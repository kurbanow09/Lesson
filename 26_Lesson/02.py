def haryt_gos(ady, bahasy, mukdary):
    with open("market_harytlary.txt", "a") as fayl:
        fayl.write(f"{ady}, {bahasy}, {mukdary}\n")

def harytlary_gorkez():
    with open("market_harytlary.txt", "r") as fayl:
        setirler = fayl.readlines()

    for setir in setirler:
        ady, bahasy, mukdary = setir.split(',')
        print(f"Ady: {ady}, \nBahasy: {bahasy}, \nMukdary: {mukdary}\n")

print("Market ulgamy!\n-----------------------")
while True:
    bolum = input("\nHaryt gosmak (i) \nHarytlary gormek (2) \nCykmak (3): \nYour choice: ")
    if bolum == "1":
        ady = input("Haryt ady: ")
        bahasy = input("Bahasy: ")
        mukdary = input("Mukdary: ")
        haryt_gos(ady, bahasy, mukdary)
    elif bolum == "2":
        harytlary_gorkez()
    elif bolum == "3":
        print("Thank you using our program!!")
        break