def wagty_bildir(sagat):
    if 0 <= sagat <= 5:
        print("Gije")
    elif 6 <= sagat <= 12:
        print("Irden")
    elif 13 <= sagat <= 18:
        print("Oylan")
    elif 19 <= sagat <= 23:
        print("Agsam")
    else:
        print("Bilemok")
  
  
sagat = int(input("Sagat naçe:"))
wagty_bildir(sagat)