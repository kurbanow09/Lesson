def sanlary_hasapla(sany):
    polozitel_sum = 0
    otrisatel_count = 0

    for i in range(sany):
        san = int(input(f'{i+1}. sany'))
        if san > 0:
            polozitel_sum += san
        elif san < 0:
            otrisatel_count += 1

    print(f'polozitellerin jemi: {polozitel_sum}')
    print(f'otrisatellerin jemi: {otrisatel_count}')


san = int(input('Nace sany: '))


sanlary_hasapla(san)
