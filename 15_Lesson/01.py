dukan = {
    'alma': 8,
    'uzum': 12,
    'hurma': 18,
    'banan': 25,
    'nar': 15,
}

for i, j in dukan.items():
    print(i, '-', j, 'Manat')
kassa = 0
while True:
    a = input('Name almak isleyaniz? ')
    if a == 'quit':
        break
    elif a in dukan:
        b = int(input('Nace kg almak isleyarniz? '))
        pul = b * dukan[a]
        kassa += pul
    elif a not in dukan:
        print(f"{a} Dukanda yok")
print(f"Siz {kassa} manat tolemeli") 