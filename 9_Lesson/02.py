cekimliler = 'aäuüoöiey'
cekimsizler = 'bçdfghjklmnňprsşwýtzž'

name = input('Name: ')
cekimli_count, cekimsiz_count, nabelli_count = 0, 0, 0

for i in name:
    if i in cekimliler:
        cekimli_count += 1
    elif i in cekimsizler:
        cekimsiz_count += 1
    else:
        nabelli_count += 1

print(f'{cekimli_count} cekimli')
print(f'{cekimsiz_count} cekimsiz')
print(f'{nabelli_count} nabelli')
