ad = input("Adynyzy yazyn: ")

cekimli = "aeiouyäöüAEIOUYÄÖÜ"
cekimli_sany = 0
cekimsiz_sany = 0

for harp in ad:
    if harp.isalpha():

        if harp in cekimli:
            cekimli_sany += 1
        else:
            cekimsiz_sany += 1

print(f"Adynyzda {cekimli_sany} sany cekimli harp bar: ")
print(f"Adynyzda {cekimsiz_sany} sany cekimsiz harp bar: ")