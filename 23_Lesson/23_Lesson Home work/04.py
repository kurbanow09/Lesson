import os


confirm = input('1 - Ady üýtgetmegi isleýärsiňizmi? (Hawa / Ýok): ').strip().lower()

if confirm == 'hawa':
    for old_name, new_name in zip(range(1, 11), range(91, 101)):
        old_folder = str(old_name)
        new_folder = str(new_name)
        
        if os.path.exists(old_folder):
            os.rename(old_folder, new_folder)
            print(f'"{old_folder}" bukjanyň ady "{new_folder}" diýip üýtgedildi.')
        else:
            print(f'"{old_folder}" atly bukja tapylmady.')
else:
    print('Bukjalaryň ady üýtgedilmedi.')