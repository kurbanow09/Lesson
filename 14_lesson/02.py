ad = input("adynyzy yazyn: ")

harp_sany = len(ad)
print(f"Adynyzdaky harp sany: {harp_sany}")

ters_ad = ad[::-2]
print(f"Adynyzy 2 harp aralykdan tersine yazdyrsanyz: {ters_ad}")

sonky_3_harpy = ad[-3:]
print(f"Adynyzyn sonky 3 harpy; {sonky_3_harpy}")

uly_harply_ad = ad.upper()
print(f"Adynyzy uly harplar bilen yazsanyz: {uly_harply_ad}")

calsylan_ad = ad.replace("a","e".replace("A","E"))
print(f"Adynyzda 'a' harplarynyn yerine 'e' goylan gornusi: {calsylan_ad}" )