import random

def tahmin_oyuny():
    print("Men bir san sayladym. siz ony tapyp bilresinizmi!")

    in_kici = int(input("in kici sany sayladynyz: "))
    in_uly = int(input("In uly sany sayladynyz: "))

    saylan_san = random.randint(in_kici, in_uly)
    synasyk = 0

    while True:
        synasyk += 1
        caklama  = int(input("Sany caklan: "))

        if caklama > saylan_san:
            print("sizin calamanyz uly.")
        elif caklama < saylan_san:
            print("sizin caklamanyz kici.")
        else:
            print(f"Dogry tapdynyz siz {synasyk} synansykda tapmagy basardynyz")
            break

tahmin_oyuny()