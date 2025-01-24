def tapan_sanlar():
    sanlar = []
    while True:
        san = int(input("Bir san girizin (Durmak ucin 0): "))
        if san == 0:
            break
        sanlar.append(san)

    if sanlar:
        in_uly = max(sanlar)
        in_kici = min(sanlar)
        return f"in uly san: {in_uly}, in kici san: {in_kici}"
    else:
        return "San girizilmedi."

print(tapan_sanlar())
