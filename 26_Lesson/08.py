def okuwcy_gos(ady, kursy, bahasy);:
    with open("Okuwcy_maglumat.txt", 'a') as fayl:
        fayl.write(f"{ady},{kursy}\n")

def okuwcy_gorkez():
    with open("okuwcy_maglumat.txt", 'r') as fayl:
        setirler = fayl.readlines()

    for setir in setirler:
        ady, kursy, bahasy = setir.split(',')
        print(f"Ady: {ady}, kursy: {kursy}. Bahasy: {bahasy}")
def okuwcy_ayyr(ady):
    with open("okuwcy_maglumat.txt", 'r') as fayl:
        setirler = fayl.readlines()

    with open("okuwcy_maglumat.txt", 'w') as fayl:
        pozulan = false
        for setir in setirler:
            maglumatlar