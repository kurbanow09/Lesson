soraglar = [
    ("Dunyan in gowy oyuncusy kim?", ["pele", "Ronaldo", "messi", "roberto carlos"], "Ronaldo"),
    ("'Ispanyan in gucli futbol kluby?", ["Real Madrid", "atletico madrid", "barcelona", "real socieded"], "Real Madrid"),
    ("Real Madrid 1943 de barcelona bilen oynasdi Real Madrid nace gol saldi?", ["1-2", "2-1", "3-1", "11-1"], "11-1"),
    ("La liga da in kan champiyon bolan klup?", ["atletico madrid", "barcelona", "Real Madrid", "real soocieded"], "Real Madrid"),
    ("Ronaldo nace yasynda futbola baslady?", ["16", "17", "18", "19"], "16"),
    ("portugalyan in gowy oyuncusy kim?", ["Rui costa", "Ricardo Carvalho", "Ronaldo", "Deco"], "Ronaldo"),
    ("fotbol da in kan gol kim atdi?", ["Ronaldo", "messi", "pele", "neymar"], "Ronaldo"),
    ("Ronaldo prime yyly hacandy?", ["2015", "2023", "2008", "2009"], "2008"),
    ("fotbol da in kan rekord goyan oyuncy kim?", ["pele", "roperto carlos", "messi", "Ronaldo"], "Ronaldo"),
    ("Ronaldo ilkinci haysy klubda oynadi?", ["sporting portugal", "mancester united", "ahal fk", "real madrid"], "sporting portugal"),
]

bal = 0
dogry_jogap_sany = 0
yalnys_jogap_sany = 0
sorag_sany = 0  

for sorag in soraglar:
    print(f"Sorag: {sorag[0]}")
    jogaplar = sorag[1]  
    dogry_jogap = sorag[2]  

    print(f"1. {jogaplar[0]}")
    print(f"2. {jogaplar[1]}")
    print(f"3. {jogaplar[2]}")
    print(f"4. {jogaplar[3]}")


    ulanyjy_jogaby = int(input("Jogabyňyzy saýlaň (1-4): ")) - 1

    if jogaplar[ulanyjy_jogaby] == dogry_jogap:
        print("Dogry jogap!")
        bal += 10  
        dogry_jogap_sany += 1
    else:
        print(f"Ýalňyş jogap! Dogry jogap: {dogry_jogap}")
        bal -= 5  
        yalnys_jogap_sany += 1

    sorag_sany += 1  


    if sorag_sany == 10:
        break

    print()  

print("")
print(f"Oýun tamamlandy! 🎉🎊🎈🎇🎆✨✨🎉 \nJemi bal: {bal}")
print(f"Dogry jogaplaryň sany: {dogry_jogap_sany}")
print(f"Ýalňyş jogaplaryň sany: {yalnys_jogap_sany}")
