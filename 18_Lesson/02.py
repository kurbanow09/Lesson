def gosmak():
    print(f"Netije: {san1 + san2}")


def ayyrmak():
    print(f"Netije: {san1 - san2}")


def kopeltmek():
    print(f"Netije: {san1 * san2}")
    

def bolmek():
    if san2 == 0:
        print(f"Netije: {san1 / san2}")

    else:
        print(f"0-a bölüp bolmaýar!")

def cykys():
    print("Cykdynyz!")



while True:
    san1 = int(input("Birinji sany girizin: "))
    san2 = int(input("Ikinji sany girizin: "))
    funksiya = input("Funksiya saylan: +, -, *, /\nFunksiya: ")
    if funksiya == "+":
        gosmak()
    elif funksiya == "-":
        ayyrmak()
    elif funksiya == "*":
        kopeltmek()
    elif funksiya == "/":
        bolmek()
    else:
        funksiya == "quit"
        cykys = input("Täzeden hasaplaýarsyňyzmy? (hawa/ýok): ").lower()
        if cykys == "hawa":
            continue
        elif cykys == "yok":
            break
            cykys()