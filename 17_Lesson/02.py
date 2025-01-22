def hasap_barlamak():
    tel_belgi = int(input('Tel belginiz '))
    if 60000000 <= tel_belgi <= 65999999 or 71000000 <= tel_belgi <= 71999999:
        print(f"Sizin hasabynyzda: 5 TMT")
    else:
        print("Yalnysh telefon belgi girizdiniz!")
        
def hasap_doldurmak():
    tel_belgi = int(input('Tel belginiz: '))
    if 60000000 <= tel_belgi <= 65999999 or 71000000 <= tel_belgi <= 71999999:
        tel_mocberi = int(input("Toleg mocberiniz (TMT): "))
        if 0 <= tel_mocberi <= 50:
            print(f"Sizin hasabynyz {5 + tel_mocberi} TMT")
        else:
            print("Toleg mukdary 1-50 TMT aralygy bolmaly!")
    else:
        print("Yalnysh telefon belgi girizdiniz!")

def cykysh():
    print("Cykdynyz")

while True:
    print("TMCELL hyzmatlary")
    print("1.Balansyny barlamak")
    print("2.Balansyny doldurmak")
    print("3.Cykmak")

    hyzmat = input('Hyzmat gornusini saylan(1, 2): ')
    if hyzmat == '1':
        hasap_barlamak()
    elif hyzmat == "2":
        hasap_doldurmak()
    elif hyzmat == "3":
        cykysh()
        break