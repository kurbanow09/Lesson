def login_system(dogry_ulanyjy, dogry_parol, maks_ymtykma):
    ymtykma_sany = 0

    while ymtykma_sany < maks_ymtykma:
        ulanyjy_ady = input("Ulanycyjy adyny girizin: ")
        parol = input("Paroly girizizn: ")

        if ulanyjy_ady == dogry_ulanyjy and parol == dogry_parol:
            print("Hos geldiniz!")
            return 
        else:
            ymtykma_sany += 1
            print("Hasaba girmage bolan mumkinciliginiz gutardy.")

login_system("user123", "Parol456", 3)