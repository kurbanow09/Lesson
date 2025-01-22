def balans_barla():
    belgi = int(input("Telefon belginiz: "))
    if (60000000 <= belgi <= 65999999 or 71000000 <= belgi <= 71999999):
        print(f"Telefon balansy: 15.0 TMT")
    else:
        print("Yalnys belgi girdiniz!")

def balans_doldur():
    belgi = int(input("Telefon belginiz: "))
    if 60000000 <= belgi <= 65999999 or 71000000 <= belgi <= 71999999:
        toleg_mocberi = int(input("Tolegin mukdaryny girizin: "))
        if 1 <= toleg_mocberi <= 50:
            print(f"Sizin balansynyz: {15.0 + toleg_mocberi} TMT ")
        else:
            print("Yalnys toleg mocberi yazdynyz!")
    else:
        print("Yalnys belgi girdiniz!")

def cykysh():
    print("Hyzmatynyz ucin sagbolun")

while True:
    print("TMcell hyzmatlaryn\n1. balansyny barlamak\n2. Balansyny doldurmak\n3. cykys")
    hyzmat = int(input("Hyzmaty giriz: "))
    if hyzmat == 1:
        balans_barla()
    elif hyzmat == 2:
        balans_doldur()
    elif hyzmat == 3:
        cykysh()
        break
    else:
        print("Nadogry hyzmat sayladynyz!")