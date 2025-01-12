sozlem = input("sozlemi girizin: ")

soz_sany = len(sozlem.split())
print(f"sozlerin sany: {soz_sany}")

e_sany = sozlem.count("e") + sozlem.count("E")
print(f"sozleminizde {e_sany} sany 'e' harpy bar: ")

ters_sozlem = sozlem[::-1]
print(f"Tersine sozlem: {ters_sozlem}")