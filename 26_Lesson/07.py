import datetime

def yazgy_gos():
    yazgy = input("To Do List? \n")
    senesi = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("ToDolist.txt", 'a') as fayl:
        fayl.write(f"{senesi} - {yazgy}\n")
    print("Yazgy gosuldy.")

def yzygiderli_gorkez():
    with open("ToDoList.txt", 'r') as fayl:
        setirler = fayl.readlines()

        if not setirler:
            print("Gunlik yazgy yok.")
        else:
            print("Gunlik yazgylar:")
            for setir in setirler:
                print(setir)


print("Gunlik Ulgamy")
while True:
    bolum = input("\nTaze yazgy gosmak (1)\nGunlik yazgylaryny gormek (2)\nCykmak (3):")
    if bolum == "1":
        yazgy_gos()
    elif bolum == "2":
        yzygiderli_gorkez()
    elif bolum == "3":
        print("Programmany ulananynyz ucin sag bolum!")
        break