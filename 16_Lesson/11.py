dukan = {
    'alma': {'bahasy' : 15, 'mukdary' : 30},
    'kiwi': {'bahasy' : 18, 'mukdary' : 1},
    'mandarin': {'bahasy' : 30, 'mukdary' : 10},
    'banan': {'bahsy' : 27, 'mukdary' : 20},
    'nar': {'bahasy' : 18, 'mukdary' : 15}

} 

kassa = 0
operation = ""

while operation != 'quit':
    print("\n***DUKAN DOLANDYRYS***")
    print("1. Kitaplary gormek")
    print("2. Haryt satym al")
    print("3. Harytlaryn gos")
    print("4. Harytlaryn bahasy uytget")
    print("5. Harytlary ayyr")
    print("6. Mukdary artdyr")
    print("7. Kassany gor")

    operation = input('Name etmeli (san girizin):')


    if operation == '1':
        print("\nKitaplary gormek: ")
        for i, j in dukan.items():
            print(f"{i} - Bahasy: {j['bahasy']} manat, Mukdary: {j['mukdary']} kg")
    


    elif operation == '2':
        haryt = input('Name satyn aljak? ')
        if haryt in dukan:
            kg = float(input(f'Nace kg {haryt} almak isleyan? '))
            if kg <= dukan[haryt]['mukdary']:
                pul = kg * dukan[haryt]['bahasy']
                kassa += pul
                dukan[haryt]['mukdary'] -= kg
                print(f"{haryt}-y satyn aldynyz {pul} manat boldy. ")
            else:
                print(f"{haryt}-yn yeterlik mukdary yok! hazirlikce {dukan['MUKDARY']} KG BAR.")
        
        else:
            print(f"{haryt} dukan yok")

    elif operation == '3':
        haryt = input('Taze haryt  ady girizin: ')
        baha = float(input(f"{haryt}-yn bahasy: "))
        mukdar = float(input(f"Nace kg {haryt} gosmaly? "))
        dukan[haryt] = {'bahasy' :  baha, 'mukdary' : mukdar}
        print(f"{haryt}-yn bahasy tazelendi.")

    elif operation == '4':
        haryt = input('haysy harydyn bahasyny uytgetmeli? ')
        if haryt in dukan:
            baha = float(input(f"{haryt}-yn bahasy: "))
            baha[haryt]['bahasy'] = baha
            print(f"{haryt}-yn bahasy tazelendi.")
            dukan[Haryt]['bahasy'] = baha
            print(f"{haryt}-yn bahasy tazelendi")
        else:
            print(f"{haryt} dukanda yok")


    elif operation == '5':
        haryt = input('Haysy harydyn ayyrmaly? ')
        if haryt in dukan:
            gosuljak_mukdar = float(input(f"Nace kg gosmaly? (onki mukdary: {dukan[haryt]['mukdary']}):"))
            dukan[haryt]['mukdary'] += gosuljak_mukdar
            print(f"{haryt}-yn mukdary tazelendi.")
        else:
            print(f"{haryt} dukanda yok")

    elif operation == 'quit':
        print("programma tamamlandy")
    else:
        print("Nadogry operasiya! Gaytadan saylan.")