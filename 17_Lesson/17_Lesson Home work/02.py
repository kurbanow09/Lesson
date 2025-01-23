dukanyň_harytlary = {
    "alma": {"bahasy": 15, "mukdary": 20},
    "banan": {"bahasy": 30, "mukdary": 10},
    "kiwi": {"bahasy": 50, "mukdary": 5},
}
kassa = 0

def harytlary_gorkez():
    if dukanyň_harytlary:
        print("\nDükandaky ähli harytlar:")
        for haryt, maglumatlar in dukanyň_harytlary.items():
            print(f"- {haryt}: {maglumatlar['bahasy']} manat/kg, {maglumatlar['mukdary']} kg")
    else:
        print("\nDükanda haryt ýok.")

def haryt_satyn_al():
    global kassa
    haryt_ad = input("\nHaýsy harydy satyn almak isleýärsiňiz? ").lower()
    if haryt_ad in dukanyň_harytlary:
        mukdar = float(input(f"Haýsy mukdary satyn alarsyňyz? (Bar: {dukanyň_harytlary[haryt_ad]['mukdary']} kg): "))
        if mukdar <= dukanyň_harytlary[haryt_ad]["mukdary"]:
            bahasy = mukdar * dukanyň_harytlary[haryt_ad]["bahasy"]
            dukanyň_harytlary[haryt_ad]["mukdary"] -= mukdar
            kassa += bahasy
            print(f"{mukdar} kg {haryt_ad} satyn aldyňyz. Töleg: {bahasy} manat.")
            if dukanyň_harytlary[haryt_ad]["mukdary"] == 0:
                del dukanyň_harytlary[haryt_ad]
        else:
            print("Bagyşlaň, bu mukdar biziň dükanymyzda ýeterlik däl.")
    else:
        print("Bu haryt dükanda ýok.")

# Täze haryt goşmak
def haryt_gos():
    haryt_ad = input("\nTäze harydyň ady: ").lower()
    if haryt_ad in dukanyň_harytlary:
        print(f"{haryt_ad} eýýäm dükanda bar. Mukdary artdyrmak üçin 6 saýlawy ulanyň.")
    else:
        bahasy = float(input("Bahasy (manat/kg): "))
        mukdary = float(input("Mukdary (kg): "))
        dukanyň_harytlary[haryt_ad] = {"bahasy": bahasy, "mukdary": mukdary}
        print(f"{haryt_ad} dükana goşuldy.")

def bahany_uytget():
    haryt_ad = input("\nHaýsy harydyň bahasyny täzeläsiňiz? ").lower()
    if haryt_ad in dukanyň_harytlary:
        täze_baha = float(input(f"Täze bahasy (önki bahasy: {dukanyň_harytlary[haryt_ad]['bahasy']} manat): "))
        dukanyň_harytlary[haryt_ad]["bahasy"] = täze_baha
        print(f"{haryt_ad} harydyň bahasy täzelendi.")
    else:
        print("Bu haryt dükanda ýok.")

def haryt_ayyr():
    haryt_ad = input("\nHaýsy harydy aýyrmaly? ").lower()
    if haryt_ad in dukanyň_harytlary:
        del dukanyň_harytlary[haryt_ad]
        print(f"{haryt_ad} harydy dükandan aýryldy.")
    else:
        print("Bu haryt dükanda ýok.")

def mukdary_artdyr():
    haryt_ad = input("\nHaýsy harydyň mukdaryny artdyrmaly? ").lower()
    if haryt_ad in dukanyň_harytlary:
        goşmaça = float(input(f"Näçe kg goşmaly? (önki mukdary: {dukanyň_harytlary[haryt_ad]['mukdary']} kg): "))
        dukanyň_harytlary[haryt_ad]["mukdary"] += goşmaça
        print(f"{haryt_ad}-yň mukdary täzelendi.")
    else:
        print("Bu haryt dükanda ýok.")

def kassany_gorkez():
    print(f"\nKassanyň jemi: {kassa} manat.")

def menu():
    print("\nDükanyň dolandyryş programmasy:")
    print("1. Harytlary görkezip bilmek")
    print("2. Haryt satyn almak")
    print("3. Täze haryt goşmak")
    print("4. Harydyň bahasyny üýtgetmek")
    print("5. Harydy aýyrmak")
    print("6. Mukdary artdyrmak")
    print("7. Kassany görkezmek")
    print("8. Programmadan çykmak")

while True:
    menu()
    saýlaw = input("\nNäme etmeli? (1-8): ")
    if saýlaw == "1":
        harytlary_gorkez()
    elif saýlaw == "2":
        haryt_satyn_al()
    elif saýlaw == "3":
        haryt_gos()
    elif saýlaw == "4":
        bahany_uytget()
    elif saýlaw == "5":
        haryt_ayyr()
    elif saýlaw == "6":
        mukdary_artdyr()
    elif saýlaw == "7":
        kassany_gorkez()
    elif saýlaw == "8":
        print("Programma tamamlandy.")
        break
    else:
        print("Nädogry saýlaw, täzeden synanyşyň.")
