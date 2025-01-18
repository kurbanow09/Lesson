# Kitap maglumatlary saklamak
kitaplar = {
    101: {'title': 'Perman', 'author': 'A.Govshudov', 'quantity': 8},
    102: {'title': 'Saylanan eserler', 'author': 'G.Ezizov', 'quantity': 12},
    103: {'title': 'Ykbal', 'author': 'H.Deryayev', 'quantity': 6},
    104: {'title': 'Leyli Mejnun', 'author': 'N.Andalyp', 'quantity': 4},
    105: {'title': 'Oylanma bayry', 'author': 'K.Gurbannepesov', 'quantity': 9},
}

# Kitaplary gormek
def kitaplary_gormek():
    for kitap_id in kitaplar:
        print(f"Kitap belgisi: {kitap_id} | Ady: {kitaplar[kitap_id]['title']} | Awtory: {kitaplar[kitap_id]['author']} | Sany: {kitaplar[kitap_id]['quantity']}")

# Kitap almak
def kitap_almak():
    kitap_id = int(input("Kitap belgisi girin: "))
    if kitap_id in kitaplar:
        sany = int(input("Nace kitap almak islersiniz? "))
        if kitaplar[kitap_id]['quantity'] >= sany:
            kitaplar[kitap_id]['quantity'] -= sany
            print(f"{kitaplar[kitap_id]['title']} kitabyndan {sany} sany alındy.")
        else:
            print("Yeterli kitap ýok.")
    else:
        print("Nadogry kitaphana belgisi.")

# Kitap tabşyrmak
def kitap_tabshyrmak():
    kitap_id = int(input("Kitap belgisi girin: "))
    if kitap_id in kitaplar:
        sany = int(input("Nace kitap yzyna tabşyrmak islersiniz? "))
        kitaplar[kitap_id]['quantity'] += sany
        print(f"{kitaplar[kitap_id]['title']} kitabyndan {sany} sany yzyna tabşyrdyň.")
    else:
        print("Nadogry kitaphana belgisi.")

# Esas menyu
while True:
    print("\n*KITAPHANA*")
    print("1.Kitaplary gormek")
    print("2.Kitap almak")
    print("3.Kitap tabşyrmak")
    print("4.Cykmak")

    saýla = input("Saylan: ")

    if saýla == '1':
        kitaplary_gormek()
    elif saýla == '2':
        kitap_almak()
    elif saýla == '3':
        kitap_tabshyrmak()
    elif saýla == '4':
        print("Sag bolun, Kitaphana gelip durun!")
        break
    else:
        print("Nadogry buyruk")