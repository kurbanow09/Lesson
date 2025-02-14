def soz_sanyny_tap(faýl_ad, gozlenyan_soz):
    try:
        with open(faýl_ad, 'r', encoding='utf-8') as fayl:
            mazmun = fayl.read().lower()
            mukdar = mazmun.count(gozlenyan_soz.lower()) 

        print(f"\nGözlenýän söz: {gozlenyan_soz}")
        if mukdar > 0:
            print(f"{gozlenyan_soz} sozüniň mukdary: {mukdar}")
        else:
            print(f"{gozlenyan_soz} sözi faýlda tapylmady.")
    
    except FileNotFoundError:
        print("Faýl tapylmady.")


gozlenyan_soz = input("Gözlemek isleýän sözüňizi giriziň: ")


faýl_ad = "Book.txt" 

soz_sanyny_tap(faýl_ad, gozlenyan_soz)